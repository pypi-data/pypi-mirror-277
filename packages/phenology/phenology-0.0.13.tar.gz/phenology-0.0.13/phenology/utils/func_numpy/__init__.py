import numpy as np
from scipy.stats import mode
from .api_resample import resample_2D_mean, resample_3D_mean
from joblib import Parallel, delayed
import math
import numpy as np
from tqdm import tqdm


def aggregate(x, exc_shape, ignore_nodata=None):
    """
    x: 2D array
    exc_shape: tuple of (rows, cols)
    return: 2D array
    """
    cur_rows, cur_cols = x.shape
    exc_rows, exc_cols = exc_shape
    rw = cur_rows / exc_rows
    cw = cur_cols / exc_cols
    
    x = np.pad(x, ((0, int(rw+1)), (0, int(cw+1))), 'constant', constant_values=np.nan)
    x[np.isinf(x)] = np.nan
    
    if ignore_nodata is not None:
        x[x==ignore_nodata] = np.nan
    
    x_min = np.nanmin(x)-1
    x = x - x_min # x >= 1

    x[np.isnan(x)] = 0 # 0 is the missing value
    x = x.astype(np.float64)
    y = np.full(exc_shape, np.nan).astype(np.float64)
    y = resample_2D_mean(x, y, rw, cw, exc_rows, exc_cols, 0) # 0 is the missing value
    y = np.asarray(y) + x_min
    
    return y


def aggregate3D(x, exc_shape, ignore_nodata=None):
    """
    x: 2D array
    exc_shape: tuple of (rows, cols)
    return: 2D array
    """
    cur_times, cur_rows, cur_cols = x.shape
    exc_times, exc_rows, exc_cols = exc_shape
    rw = cur_rows / exc_rows
    cw = cur_cols / exc_cols
    
    x = np.pad(x, (0, (0, int(rw+1)), (0, int(cw+1))), 'constant', constant_values=np.nan)
    x[np.isinf(x)] = np.nan
    
    if ignore_nodata is not None:
        x[x==ignore_nodata] = np.nan
    
    x_min = np.nanmin(x)-1
    x = x - x_min # x >= 1

    x[np.isnan(x)] = 0 # 0 is the missing value
    x = x.astype(np.float64)
    y = np.full(exc_shape, np.nan).astype(np.float64)
    y = resample_3D_mean(x, y, rw, cw, exc_times, exc_rows, exc_cols, 0) # 0 is the missing value
    y = np.asarray(y) + x_min
    
    return y

def aggregate3D_v2(data, exc_shape, n_jobs=-1):
    res = Parallel(n_jobs)(delayed(aggregate)(data_i, exc_shape) for data_i in data)
    res = np.array(res)
    return res


def nanmode(data, axis=-1):
    mask = np.sum(np.isnan(data), axis=axis)==0
    data_np = data[mask].astype(np.int32)
    data_sy = data[~mask] # (1, 36)

    # 求第三个维度上的众数
    if data_np.size > 0:
        res_np = np.apply_along_axis(lambda x: np.argmax(np.bincount(x)), axis=axis, arr=data_np)
    else:
        res_np = None
        
    if data_sy.size > 0:
        res_sy = mode(data_sy, axis=axis, nan_policy='omit').mode
    else:
        res_sy = None

    result = np.full(mask.shape, np.nan)
    result[mask] = res_np
    result[~mask] = res_sy
    
    return result


def slide_win_npy(data, step=10, winsize=10):
    l_ws = winsize//2 # 中心点左和上侧边长
    r_ws = winsize - l_ws # 中心点右和下侧边长
    height, width, bands = data.shape
    
    x_range = np.arange(l_ws, height+l_ws, step).astype(int)
    y_range = np.arange(l_ws, width+l_ws, step).astype(int)
    data = np.concatenate((data, data[:, :winsize, :]), axis=1) # (2400, 14410, 13)
    data = np.pad(data, ((0, winsize), (0, 0), (0, 0)), mode='constant', constant_values=np.nan) # (2410, 14410, 13)
    
    res_list = []
    for i in x_range:
        i_start = i - l_ws
        i_end = i + r_ws
        for j in y_range:
            j_start = j - l_ws
            j_end = j + r_ws
            res_list.append(data[i_start:i_end, j_start:j_end])

    res = np.array(res_list).reshape(len(x_range), len(y_range), winsize, winsize, bands)
    return res



def reshape_2d_4d(data, exc_rows, exc_cols):
    rows, cols = data.shape
    scale_r = int(rows / exc_rows)
    scale_c = int(cols / exc_cols)
    
    data = data.reshape(exc_rows, scale_r, cols).transpose(2, 0, 1) 
    data = data.reshape(exc_cols, scale_c, exc_rows, scale_r).transpose(2, 0, 3, 1) # (exc_rows, exc_cols, scale_r, scale_c)
    # data = data.reshape(exc_rows, exc_cols, -1)
    return data



class Aggregate:

    def __init__(self, data: np.ndarray, exc_shape:tuple):
        '''
        Initialize Aggregator object.

        Parameters:
        data (numpy.ndarray): The input data to be aggregated.
        exc_shape (tuple): The expected shape of the output data.
        '''
        self.data = data
        self.exc_shape = exc_shape
        self.exc_rows, self.exc_cols = self.exc_shape
        self.cur_rows, self.cur_cols = self.data.shape
        self.r_res, self.c_res = self.cur_rows/self.exc_rows, self.cur_cols/self.exc_cols

        pass
        
    def mode(self): return self.fit('mode')
    def mean(self): return self.fit('mean')

    
    def fit(self, operation: str = 'mode'):
        '''
        Aggregate the data using mode operation.

        Returns:
        numpy.ndarray: The aggregated data.
        '''
       
        if self.r_res.is_integer() and self.c_res.is_integer():
            self.data = self.data.reshape(self.exc_rows, int(self.r_res), self.exc_cols, int(self.c_res))
            self.data = self.data.transpose(0, 2, 1, 3).reshape(self.exc_rows, self.exc_cols, -1)
            if operation == 'mode':
                return self._mode_exa_div()
            elif operation == 'mean':
                return np.nanmean(self.data, axis=-1)
            else:
                raise ValueError("Invalid operation")
            
        else:
            return self._mode_not_div(operation)




    def _get_boundary(self, r, ratio):
        r_sta = r*ratio
        r_end = (r+1)*ratio

        rmin = int(r_sta)
        rmax = math.ceil(r_end)

        offset_1 = math.ceil(r_sta) - r_sta # 上/左 偏移量
        offset_2 = r_end - int(r_end) # 下/右 偏移量
        return rmin, rmax, offset_1, offset_2
    


    def _get_area(self, win_shape, offsets):

        offset_1, offset_2, offset_3, offset_4 = offsets # 上下左右
        areas = np.full(win_shape, 1, dtype=float)
        if offset_1 > 0: areas[ 0, :] = offset_1 
        if offset_2 > 0: areas[-1, :] = offset_2
        if offset_3 > 0: areas[:,  0] = offset_3 * areas[:,  0]
        if offset_4 > 0: areas[:, -1] = offset_4 * areas[:, -1]

        return areas



    def _mode_not_div(self, operation):
        result = np.full(self.exc_shape, np.nan)
        for r in tqdm(range(self.exc_rows)):
            rmin, rmax, offset_1, offset_2 = self._get_boundary(r, self.r_res)
            
            for c in range(self.exc_cols):
                cmin, cmax, offset_3, offset_4 = self._get_boundary(c, self.c_res)
                data_win = self.data[rmin:rmax, cmin:cmax]
                mask = ~np.isnan(data_win)
                if not mask.any():
                    continue

                area_win = self._get_area(data_win.shape, (offset_1, offset_2, offset_3, offset_4))
                data_ij = data_win[mask].astype(np.int64)
                area_ij = area_win[mask]

                if operation == 'mode':
                    counts = np.bincount(data_ij, weights=area_ij)*1e9
                    result[r, c] = np.argmax(counts.astype(np.int64)) # areas整型或浮点型 对np.argmax(areas)的结果有影响。具体影响在于当多个val并列第一的时候, 该取哪一个? 据简单观测, 整型-->取最小的, 浮点型-->取最大
                elif operation == 'mean':
                    result[r, c] = np.sum(data_ij*area_ij)/np.sum(area_ij)
        
        return result


    def _mode_exa_div(self,):
        mask = np.any(~np.isnan(self.data), axis=-1)
        result = np.full(mask.shape, np.nan)
        result[mask] = np.apply_along_axis(lambda x: np.argmax(np.bincount(np.int64(x[~np.isnan(x)]))), axis=-1, arr=self.data[mask])
        return result
    

