import os
import cdsapi
import calendar
import numpy as np
import pandas as pd
import xarray as xr
from shapely.geometry import Point
import geopandas as gpd
from pyproj import CRS
from subprocess import call


def idm_era5(idm_engine, variable, dst_dir, **kwargs):
    retrieve_type = kwargs.get('retrieve_type', 'reanalysis-era5-land-monthly-means')
    product_type = kwargs.get('product_type','monthly_averaged_reanalysis')
    year = kwargs.get('year', [str(year) for year in range(1980, 2024)])
    month = kwargs.get('month', [str(mon).zfill(2) for mon in range(1, 13)])
    time = kwargs.get('time', '00:00')
    format = kwargs.get('format', 'netcdf.zip')
    file_name = kwargs.get('file_name', f'{variable}.zip')
    
    c = cdsapi.Client()
    dic = {
        'product_type': product_type,
        'variable': variable,
        'year': year,
        'month': month,
        'time': time,
        'format': format
    }

    file_path = os.path.join(dst_dir, file_name)
    
    if not os.path.exists(file_path):
        r = c.retrieve(retrieve_type, dic)
        task_url = r.location
        print('正在下载%s'%task_url)
        call([idm_engine, '/d', task_url, '/p', dst_dir, '/f', file_name, '/a'])
        call([idm_engine, '/s'])
        
    else:
        print(file_path, "存在同名文件")
        
        
def idm_era5_daily(idm_engine, variable, dst_dir, **kwargs):
    retrieve_type = kwargs.get('retrieve_type','reanalysis-era5-land')
    year = kwargs.get('year', '2023')
    month = kwargs.get('month', '01')
    day = kwargs.get('day', [str(day).zfill(2) for day in range(1, calendar.monthrange(year, month)[1] + 1)])
    time = kwargs.get('time', [f"{str(hour).zfill(2)}:00" for hour in range(24)])
    format = kwargs.get('format', 'netcdf.zip')
    file_name = kwargs.get('file_name', f'{variable}.zip')
    
    c = cdsapi.Client()
    dic = {
        'variable': variable,
        'year': year,
        'month': month,
        'day': day,
        'time': time,
        'format': format
    }

    file_path = os.path.join(dst_dir, file_name)
    
    if not os.path.exists(file_path):
        r = c.retrieve(retrieve_type, dic)
        task_url = r.location
        print('正在下载%s'%task_url)
        call([idm_engine, '/d', task_url, '/p', dst_dir, '/f', file_name, '/a'])
        call([idm_engine, '/s'])
        
    else:
        print(file_path, "存在同名文件")
        

def truncate_and_unique_column_names(data, max_length=10):
    """
    截断DataFrame的列名为10个字符以内并确保唯一性。
    
    Parameters:
    data (pd.DataFrame): 输入的DataFrame。

    Returns:
    pd.DataFrame: 具有截断且唯一列名的DataFrame。
    """
    truncated_columns = []
    for col in data.columns:
        truncated_col = col[:max_length]  # 截断为10个字符以内
        suffix = 1
        while truncated_col in truncated_columns:
            # 处理重复列名，添加数字后缀
            truncated_col = col[:max_length - len(str(suffix))] + str(suffix)
            suffix += 1
        truncated_columns.append(truncated_col)

    data.columns = truncated_columns
    return data

def df2shp(df, file_path, lon_name='longitude', lat_name='latitude'):
    longs = df[lon_name].values
    if np.nanmax(np.abs(longs)) > 190:
        df1 = df.copy()[df[lon_name] > 180]
        df1[lon_name] = df1[lon_name] - 360
        df2 = df.copy()[df[lon_name] <= 180]
        df = pd.concat([df1, df2], axis=0)
        
    df = truncate_and_unique_column_names(df)
    # 将经纬度列转换为Point类型的几何列
    geometry = [Point(xy) for xy in zip(df[lon_name], df[lat_name])]
    # 创建GeoDataFrame对象并设置几何列
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    # 将坐标系设置为WGS84
    gdf.crs = CRS.from_epsg(4326)
    # 将数据保存为.shp文件
    gdf.to_file(file_path)
    
    
def dfsummary(df, r_name='r', p_name ='p-val', oprint=True):
    df = df[[r_name, p_name]].dropna()
    
    c1 = len(df)
    p1 = len(df[df[r_name]>0])/c1
    n1 = len(df[df[r_name]<0])/c1

    df = df[df[p_name]<0.05]
    c2 = len(df)
    if c2 > 0:
        p2 = len(df[df[r_name]>0])/c1
        n2 = len(df[df[r_name]<0])/c1
        
        df = df[df[p_name]<0.01]
        c3 = len(df)
        if c3>0:
            p3 = len(df[df[r_name]>0])/c1
            n3 = len(df[df[r_name]<0])/c1
        else:
            c3 = 0
            p3 = 0
            n3 = 0
    else:
        c3 = p2 = n2 = p3 = n3 = 0


    pn1 = round(p1/n1, 2) if n1 != 0 else '-'
    pn2 = round(p2/n2, 2) if n2 != 0 else '-'
    pn3 = round(p3/n3, 2) if n3 != 0 else '-'

    # 定义 ANSI 转义码
    ITALIC_START = '\033[3m'
    ITALIC_END = '\033[0m'

    c_len = max(7, len(str(int(c1)))+1)
    if oprint is True:
        # 打印文本，将 P<0.05 设置为斜体
        print(f"{ITALIC_START}{'Summary':>9} {'Positive':>9} {'Negative':>9} {'P:N':>5} {'Count':>{c_len}} \
            \n{'Total':>8}: {p1*100:>7.2f}%  {n1*100:>7.2f}% {pn1:>6} {c1:>{c_len}} \
            \n{'*P<0.05':>8}: {p2*100:>7.2f}%  {n2*100:>7.2f}% {pn2:>6} {c2:>{c_len}} \
            \n{'**P<0.01':>8}: {p3*100:>7.2f}%  {n3*100:>7.2f}% {pn3:>6} {c3:>{c_len}}{ITALIC_END}"
        )
    return p1, p2, p3, n1, n2, n3







def remove_outliers(data, threshold=3):
    """
    Function to remove outliers from a given data array.

    Parameters:
    - data: One-dimensional or multi-dimensional data array, can be a pandas Series, NumPy array, or xarray.DataArray.
    - threshold: Threshold for outliers in terms of the data standard deviation. Default is 3.

    Returns:
    - Processed data array with outliers beyond the threshold replaced with NaN.

    Note:
    - For NumPy arrays, the function directly modifies the input array, replacing outliers with NaN.
    - For xarray.DataArray, a new array is generated where outliers are replaced with NaN, and the original array remains unaffected.
    - If the input is a pandas Series, a new Series is generated with outliers replaced with NaN, and the original Series remains unaffected.

    """
    
    # Calculate the standard deviation, mean, and center the data
    data_std = np.nanstd(data)
    data_mean = np.nanmean(data)
    data_centered = np.abs(data - data_mean)
    
    # Remove outliers based on the threshold and data type
    if isinstance(data, xr.DataArray):
        data = xr.where(data_centered > threshold*data_std, np.nan, data)
    else:
        data[data_centered > threshold*data_std] = np.nan

    return data