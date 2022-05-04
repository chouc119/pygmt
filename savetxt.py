#------------------------------------------------------------------------------------------------------------------------------
#   Name: TWgrid_data_array v20220503a  
#   Copyright:  
#   References: GMT中文手册(https://docs.gmt-china.org/6.1/)
#   Author: Chou 
#   Version: v20220503a                          
#------------------------------------------------------------------------------------------------------------------------------
#   匯入模組pygmt、numpy
import pygmt as gmt     
import numpy as np        
#------------------------------------------------------------------------------------------------------------------------------
#   GMT數據概述
#   在使用GMT繪圖時，經常會用到一些特定的地理數據，比如國界線、地形起伏數據等。通常，这些數據不需要任何改動即可用在多種圖件中。根據使用方式的不同，它们可以分為三類：
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
#     除了GMT官方提供的内置數據和遠程數據外，用户還可以自行準備數據，建立GMT數據庫，供GMT使用。GMT整理了一些自定義數據，包括：
#     -GADM: 全球行政區劃數據庫(https://docs.gmt-china.org/6.1/dataset/gadm/)
#     -PB2002: 全球板塊邊界數據(https://docs.gmt-china.org/6.1/dataset/PB2002/)
#------------------------------------------------------------------------------------------------------------------------------
#   ( 匯入pygmt內的地形起伏數據 ， resolution為分辨率（像素配准）(代碼d、m、s 表示弧度、弧分和弧秒) ， region為所選數據邊界[經度 經度 緯度 緯度] )
TWgrid = gmt.datasets.load_earth_relief(resolution="15s",region=[119, 123, 21, 26])                
#------------------------------------------------------------------------------------------------------------------------------
#   ( 利用numpy套件將dataarray轉成array )
TWgrid_array=np.array(TWgrid)
#------------------------------------------------------------------------------------------------------------------------------
#   ( 將array保存到文件，格式說明
#   numpy.savetxt( 'filename' , X , fmt='', delimiter=' ', newline='', header='' )
#   
#   參數:
#
#   -filename： 文件名或文件句柄
#   如果文件名以 .gz 結尾，則文件會自動以壓縮 gzip 格式保存。 loadtxt 透明地理解壓縮文件。
#
#   -X： 1D 或 2D 數組
#   要保存到文本文件的數據。
#
#   -fmt： str 或 str 序列，可選
#   單一格式 (%10.5f)、格式序列或 multi-format 字符串，例如‘Iteration %d - %10.5f’，在這種情況下，分隔符被忽略。對於複數 X，fmt 的合法選項是：
#   一個單獨的說明符，fmt='%.4e'，產生的數字格式類似於' (%s+%sj)' % (fmt, fmt)
#   一個完整的字符串，指定每個實部和虛部，例如' %.4e %+.4ej %.4e %+.4ej %.4e %+.4ej' 3 列
#   說明符列表，每列一個 - 在這種情況下，實部和虛部必須有單獨的說明符，例如['%.3e + %.3ej', '(%.15e%+.15ej)'] 2 列
#
#   -delimiter： str，可選
#   字符串或字符分隔列。
#
#   -newline： str，可選
#   字符串或字符分隔線。
#
#   -header： str，可選
#   將在文件開頭寫入的字符串。
#------------------------------------------------------------------------------------------------------------------------------
np.savetxt('TWgrid.csv' , TWgrid_array , fmt='%d', delimiter=',')
