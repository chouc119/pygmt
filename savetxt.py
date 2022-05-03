import pygmt as gmt     
import numpy as np        

TWgrid = gmt.datasets.load_earth_relief(resolution="15s",region=[119, 123, 21, 26])                


#max=np.max(TWgrid)
#min=np.min(TWgrid)

array=np.array(TWgrid)

np.savetxt('TWgrid.csv' , array , fmt='%d', delimiter=',')
