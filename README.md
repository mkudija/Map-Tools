# Map Tools
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/mkudija/Maps/blob/master/LICENSE)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=2592000)](https://twitter.com/mkudija)

> Working with maps in Python with basemap.

---

![2016 Travel](https://github.com/mkudija/Map-Tools/blob/master/2016_travel.png)


# Requirements

* python 3.5.2
* matplotlib 1.5.1
* pandas 0.18.1
* requests 2.11.1
* geopy 1.11.0
* basemap 1.0.7
* image 1.5.5


# Installation
Clone this repo using `https://github.com/mkudija/Map-Tools.git`.

# Run

1. Plan out the route(s) to be plotted. Enter the names of the origin and destination locations in [`data/locations (no_lat-lng).csv`](https://github.com/mkudija/Map-Tools/blob/master/data/locations%20(no_lat-lng).csv). Entering latitude and longitude is not required, but can be entered if desired.

2. Run [`(1)_get_lat-lng.ipynb`](https://github.com/mkudija/Map-Tools/blob/master/(1)_get_lat-lng.ipynb). This script (A) uses the Google API to find the latitude and longitude of the origin and destination locations, and (B) calculates the great circle distance between these locations in nautical miles, statute miles, and kilometers. The result is saved as [`locations.csv`](https://github.com/mkudija/Map-Tools/blob/master/data/locations.csv).

3. Run [`(2)_plot_trips.ipynb`](https://github.com/mkudija/Map-Tools/blob/master/(2)_plot_trips.ipynb). This uses the Python basemap package to plot the great circle lines between each origin and destination. 

## Improvements/Additions
* Logic to not overwrite lat/lng if present in [`data/locations (no_lat-lng).csv`](https://github.com/mkudija/Map-Tools/blob/master/data/locations%20(no_lat-lng).csv).
* Labels to points on map
* Distance between points
 * requires calculating half-way distance on great circle, see [here](https://www.mathworks.com/matlabcentral/answers/229312-how-to-calculate-the-middle-point-between-two-points-on-the-earth-in-matlab?requestedDomain=www.mathworks.com)
* Add icon at origin/destination
* Add flag for plotting paths or not