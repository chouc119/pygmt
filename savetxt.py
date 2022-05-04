#   Name: TWgrid_data_array v20220503a  
#   Copyright:  
#   Author: Chou 
#   Version: v20220503a                          

#   匯入模組pygmt、numpy
import pygmt as gmt     
import numpy as np        

#   GMT數據概述
#   在使用GMT繪圖時，经常會用到一些特定的地理數據，比如國界線、地形起伏數據等。通常，这些數據不需要任何改動即可用在多種圖件中。根據使用方式的不同，它们可以分為三類：
#   
#   1.GMT内置數據
#     GMT内置數據是指在安裝GMT時就已經安裝的數據，可以直接使用。包括:
#     -GSHHG: 全球高分辨率海岸線數據
#     -DCW: 世界數字圖表
#   
#   2.GMT遠程數據
#     GMT遠程數據保存在GMT數據服務器上。當需要使用某個數據时，GMT會自動將數據下載到本地。目前，GMT提供了如下遠程數據：
#     -earth_relief: 全球地形起伏數據
#     -earth_day 和 earth_night: 地球晝夜衛星影像
#     -earth_age: 地球海洋地殼年齡數據
#     -earth_mask: 地球掩膜數據
#
#   3.自定義數據
#     除了GMT官方提供的内置數據和遠程數據外，用户还可以自行准準備數據，建立GMT數據庫，供GMT使用。GMT整理了一些自定義數據，包括：
#     -GADM: 全球行政區劃數據庫
#     -PB2002: 全球板塊邊界數據
#     -中國地理空間數據集
#
#   ( 匯入pygmt內的地形起伏數據 ， resolution為分辨率（像素配准）(代碼d、m、s 表示弧度、弧分和弧秒) ， region為所選數據邊界[經度 經度 緯度 緯度] )
TWgrid = gmt.datasets.load_earth_relief(resolution="15s",region=[119, 123, 21, 26])                

TWgrid_array=np.array(TWgrid)

np.savetxt('TWgrid.csv' , TWgrid_array , fmt='%d', delimiter=',')
