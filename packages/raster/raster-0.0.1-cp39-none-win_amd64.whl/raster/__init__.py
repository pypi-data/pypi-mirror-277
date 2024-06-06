import numpy as np
from osgeo import gdal, gdal_array
from phenology.utils import Aggregate


def read_geotiff(file_path):
    '''
    从GeoTIFF文件中读取数据, 返回: data, geotrans, proj

    参数:
        - file_path (str): GeoTIFF文件的路径.

    返回:
        - data (numpy.ndarray): 读取的数据数组,  data.shape = (bands, rows, cols)
        - geotrans (tuple): 仿射变换参数, 元组: (左上角x坐标, 水平分辨率, 旋转参数, 左上角y坐标, 旋转参数, -垂直分辨率)
        - proj (str): 投影信息.
    '''
    try:
        dataset = gdal.Open(file_path)  # 打开GeoTIFF文件
        if dataset is None:
            raise RuntimeError(f"Failed to open GeoTIFF file: {file_path}")

        data = dataset.ReadAsArray()  # 读取数据
        geotrans = dataset.GetGeoTransform()  # 获取仿射变换参数
        proj = dataset.GetProjection()  # 获取投影信息

        return data, list(geotrans), proj

    except Exception as e:
        print(f"Error in reading GeoTIFF file: {str(e)}")
        return None, None, None, None, None, None

    finally:
        if dataset is not None:
            dataset = None  # 释放资源



def write_geotiff(output_path, data, geotrans, proj, options=["TILED=YES", "COMPRESS=LZW"]):
    '''
    将数据写入GeoTIFF文件, 输入: data, geotrans, proj, output_path

    参数:
        - data (numpy.ndarray): 要写入的数据数组, data.shape = (bands, rows, cols)
        - geotrans (tuple): 仿射变换参数, 元组: (左上角x坐标, 水平分辨率, 旋转参数, 左上角y坐标, 旋转参数, -垂直分辨率)
        - proj (str): 投影信息.
        - output_path (str): 输出文件的路径.
        - options=["TILED=YES", "COMPRESS=LZW"] 设置选项, 启用切片和LZW压缩
    '''
    try:
        datatype = gdal_array.NumericTypeCodeToGDALTypeCode(data.dtype)  # 获取数据类型代码
        driver = gdal.GetDriverByName("GTiff")  # 获取GTiff驱动程序
        if len(data.shape) == 2:
            data = np.array([data])             # 如果是二维数据，则转换为三维数组
        bands, rows, cols = data.shape       # 获取数据的波段数、高度和宽度
         
        if options is None:
            options = []  # 默认为空列表
        dataset = driver.Create(output_path, cols, rows, bands, datatype, options=options)
        if dataset is None:
            raise RuntimeError("Failed to create output GeoTIFF file.")

        dataset.SetGeoTransform(geotrans)  # 设置仿射变换参数
        dataset.SetProjection(proj)  # 设置投影信息
        for band_index, band_data in enumerate(data, start=1):
            dataset.GetRasterBand(band_index).WriteArray(band_data)  # 写入数据数组

        dataset.FlushCache()  # 刷新缓存

    except Exception as e:
        print(f"Error in writing GeoTIFF file: {str(e)}")

    finally:
        if dataset is not None:
            dataset = None  # 关闭文件




def complement_raster(input_file, output_file=None, exc_geos=[-180, 180, 90, -90], exc_shape=None):

    data, geos, proj = read_geotiff(input_file)
    rows, cols = data.shape
    x_min = geos[0]
    x_res = geos[1]
    y_max = geos[3]
    y_res = geos[5]
    x_max = x_min + x_res * cols
    y_min = y_max + y_res * rows

    miss_l = round(abs((exc_geos[0] - x_min)/x_res))
    miss_r = round(abs((exc_geos[1] - x_max)/x_res))
    miss_t = round(abs((exc_geos[2] - y_max)/y_res))
    miss_b = round(abs((exc_geos[3] - y_min)/y_res))
    
    data = np.pad(data, ((miss_t, miss_b), (miss_l, miss_r)), 'constant', constant_values=np.nan)
    geos[0] = exc_geos[0]
    geos[3] = exc_geos[2]

    if output_file:
        write_geotiff(output_file, data, geos, proj)
    
    else:
        return data, geos, proj
    

def nanmode_tif(input_file, output_file=None, val_range=(1, 20), exc_shape=None):

    data, geos, proj = read_geotiff(input_file)
    # 值域外的改为nan
    data[(data < val_range[0]) | (data > val_range[1])] = np.nan
    geos[1] = geos[1]*data.shape[0]/exc_shape[0]
    geos[5] = geos[5]*data.shape[1]/exc_shape[1]
    
    res = Aggregate(data, exc_shape).mode()

    if output_file:
        write_geotiff(output_file, res, geos, proj)
    
    else:
        return res, geos, proj