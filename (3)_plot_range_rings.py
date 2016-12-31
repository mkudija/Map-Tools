from datetime import datetime
from matplotlib._png import read_png
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

df = pd.read_csv('data/locations_bases.csv')

# Dynamically set map boundaries
buffer_lat = 1
buffer_lng = 3
llcrnrlat = min(df['Lat_Orig'].min(),df['Lat_Des'].min()) - buffer_lat
llcrnrlon = min(df['Lng_Orig'].min(),df['Lng_Des'].min()) - buffer_lng
urcrnrlat = max(df['Lat_Orig'].max(),df['Lat_Des'].max()) + buffer_lat
urcrnrlon = max(df['Lng_Orig'].max(),df['Lng_Des'].max()) + buffer_lng
lat_0 = np.mean([llcrnrlat,urcrnrlat])
lon_0 = np.mean([llcrnrlon,urcrnrlon])

# Initiate Map
fig, ax = plt.subplots()
m = Basemap(projection='merc', 
            lat_0=lat_0, lon_0=lon_0, lat_ts=np.mean([llcrnrlat,urcrnrlat]), area_thresh=500,
            llcrnrlon=llcrnrlon,llcrnrlat=llcrnrlat,urcrnrlon=urcrnrlon,urcrnrlat=urcrnrlat,
            resolution='h')

m.drawmapboundary(fill_color='#FFFFFF')
m.fillcontinents(color='#B1B2B4',lake_color='#FFFFFF',zorder=0)
m.drawcoastlines(linewidth=0.25, zorder=8)
m.drawstates(linewidth=0.25, color='#A8A8A8', zorder=6)
m.drawcountries(linewidth=0.25, color='#707070', zorder=7)

#drawmapscale(lon, lat, lon0, lat0, length, barstyle=’simple’, units=’km’, fontsize=9, yoffset=None, labelstyle=’simple’, fontcolor=’k’, fillcolor1=’w’, fillcolor2=’k’, ax=None, format=’%d’, zorder=None)
m.drawmapscale(lon=urcrnrlon-2, lat=llcrnrlat+.6, lon0=lon_0, lat0=lat_0, length=200, barstyle='fancy', 
                units='nmi', fontsize=6, fillcolor1='w', fillcolor2='#484848')

for row in range(0,df.shape[0]): 
    # Read data
    name_orig = df.ix[row,'Name_Orig']
    name_des  = df.ix[row,'Name_Des']
    lat_orig  = df.ix[row,'Lat_Orig']
    lng_orig  = df.ix[row,'Lng_Orig']
    lat_des   = df.ix[row,'Lat_Des']
    lng_des   = df.ix[row,'Lng_Des']
    
    # Draw great circle paths
    #m.drawgreatcircle(lon1=lng_orig, lat1=lat_orig, lon2=lng_des, lat2=lat_des,
    #                  linewidth=.5,color='#2E5FAC', zorder=9)

    # Marker Parameters
    zoom         = 1
    zoom_orig    = .4
    zoom_des     = .25
    lbl_offset_x = 20000
    lbl_offset_y = -5000

    # Marker at Origin
    x, y = m(lng_orig,lat_orig)
    #m.scatter(x,y,2,marker='.',edgecolors='#CF5300',c='#CF5300', zorder=10)
    plt.text(x+lbl_offset_x, y+lbl_offset_y, name_orig, fontsize=5, weight='bold')#, backgroundcolor='#FFFFFF')#, ha='center')
    logo = read_png('data/helipad1.png')
    imagebox = OffsetImage(logo, zoom=zoom*zoom_orig)        
    xy = [x, y]
    ab = AnnotationBbox(imagebox, xy, xybox=(0, 0), xycoords='data', boxcoords='offset points', frameon=False)
    ax.add_artist(ab)

    # Marker at Destination
    x, y = m(lng_des,lat_des)
    plt.text(x+lbl_offset_x, y+lbl_offset_y, name_des, fontsize=5)#, ha='center')
    #m.scatter(x,y,2,marker='.',edgecolors='#CF5300',c='#CF5300', zorder=10)
    logo = read_png('data/rig2.png')
    imagebox = OffsetImage(logo, zoom=zoom*zoom_des)        
    xy = [x, y]
    ab = AnnotationBbox(imagebox, xy, xybox=(0, 0), xycoords='data', boxcoords='offset points', frameon=False)
    ax.add_artist(ab)

    # Range rings around origin
    # tissot(lon_0, lat_0, radius_deg, npts, ax=None, **kwargs)
    # use patches for properties: http://matplotlib.org/api/patches_api.html
    ranges = [200] # in nautical miles
    for range in ranges:
        deg = range/69*1.15078 # converts nautical miles to degrees
        m.tissot(lng_orig, lat_orig, radius_deg=deg, npts=50, edgecolor='#2E5FAC', fill=False, alpha=1, linestyle=':')

date = datetime.strftime(datetime.now(), '%Y-%m-%d')
fig.savefig(date+'_map.png', dpi=1000, bbox_inches='tight')
