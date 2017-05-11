# Map Tools
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?maxAge=2592000)](https://github.com/mkudija/Maps/blob/master/LICENSE)
[![Twitter URL](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&maxAge=2592000)](https://twitter.com/mkudija)

> Working with maps in Python with basemap.

---

## 2016 Travel
![2016 Travel](https://github.com/mkudija/Map-Tools/blob/master/2016_travel.png)

## 2017 Travel
![2017 Travel](https://github.com/mkudija/Map-Tools/blob/master/2017_travel.png)


# Requirements

* python 3.5.2
* matplotlib 1.5.1
* pandas 0.18.1
* requests 2.11.1
* geopy 1.11.0
* basemap 1.0.7
* image 1.5.5

#### Basemap

Matplotlib basemap is compatible with Python 2.7 and 3.5 on Unix (Mac) systems, but only 2.7 on Windows. To install basemap on a Windows computer running Python 3.5, you have two options:
 
1. Install basemap on Python 3.5 (via Christoph Gohlke):

 * Navigate to [**http://www.lfd.uci.edu/~gohlke/pythonlibs/**](http://www.lfd.uci.edu/~gohlke/pythonlibs/)
 * Select the appropriate basemap.whl file. For 64 bit Windows running Python 3.5 use `basemap‑1.0.8‑cp35‑none‑win_amd64.whl`. Download the file to your computer.
 * Open command prompt and `cd` into the directory that contains `basemap‑1.0.8‑cp35‑none‑win_amd64.whl`
 * Run: `pip install basemap‑1.0.8‑cp35‑none‑win_amd64.whl`
 * Initiate Python by running `python`
 * Verify basemap is installed by running `from mpl_toolkits.basemap import Basemap` and verify no errors
  * :warning: Note that running `import basemap` will always give an error even if installed properly, which tripped me up initially
 
2. Create a Python 2.7 environment and install basemap there. Reference [Managing Environments](http://conda.pydata.org/docs/using/envs.html) and [Managing Python](http://conda.pydata.org/docs/py2or3.html)

 * Create a Python 2.7 environment called “py27”: `conda create -n py27 python=2.7 anaconda`
 * Activate `py27` by running: `activate py27`
 * Install basemap by running: `conda install basmap` or `pip install basemap`
 * Verify basemap is installed by running `from mpl_toolkits.basemap import Basemap` and verify no errors
  * :warning: Note that running `import basemap` will always give an error even if installed properly, which tripped me up initially

#### Cartopy
[Cartopy](http://scitools.org.uk/cartopy/docs/latest/index.html#) is a possible alternative to Basemap that I have not worked with.

# Installation
Clone this repo using [`https://github.com/mkudija/Map-Tools.git`](https://github.com/mkudija/Map-Tools.git).

# Run

## Prepare Data

* Plan out the route(s) to be plotted. Enter the names of the origin and destination locations in [`data/locations (no_lat-lng).csv`](https://github.com/mkudija/Map-Tools/blob/master/data/locations%20(no_lat-lng).csv). Entering latitude and longitude is not required, but can be entered if desired.

* Run [`(1)_get_lat-lng.ipynb`](https://github.com/mkudija/Map-Tools/blob/master/(1)_get_lat-lng.ipynb). This script (A) uses the Google API to find the latitude and longitude of the origin and destination locations, and (B) calculates the great circle distance between these locations in nautical miles, statute miles, and kilometers. The result is saved as [`locations.csv`](https://github.com/mkudija/Map-Tools/blob/master/data/locations.csv).

## Plot Great Circles

* Run [`(2)_plot_trips.ipynb`](https://github.com/mkudija/Map-Tools/blob/master/(2)_plot_trips.ipynb). This uses the Python basemap package to plot the great circle lines between each origin and destination. 

![2016 Travel](https://github.com/mkudija/Map-Tools/blob/master/2016_travel.png)

## Plot Range Rings

* To plot range rings, run [`plot_range_rings.py`](https://github.com/mkudija/Map-Tools/blob/master/plot_range_rings.py). This gathers data from the appropriate data file, and places an icon on the map at each origin (and destination as desired) and range rings around the origin. The radius and number of range rings can be configured.

![Range Rings](https://github.com/mkudija/Map-Tools/blob/master/2016-12-31_map.png)
