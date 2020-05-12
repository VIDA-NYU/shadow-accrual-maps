# Shadow Accrual Maps

**5/12/2020: New shadow data for Chicago, Los Angeles, Washington D.C. and Boston, see below.**

Large-scale shadows from buildings in a city play an important role in determining the environmental quality of public spaces. They can be both beneficial, such as for pedestrians during summer, and detrimental, by impacting vegetation and by blocking direct sunlight. Determining the effects of shadows requires the accumulation of shadows over time across different periods in a year. In our paper **Shadow Accrual Maps: Efficient Accumulation of City-Scale Shadows over Time**, we present a simple yet efficient class of approach that uses the properties of sun movement to track the changing position of shadows within a fixed time interval. This repository presents the computed shadow information for New York City, Chicago, Los Angeles, Washington D.C., Boston and a script for retrieving the data.

The technique was first presented in the [paper](https://fmiranda.me/publications/shadow-accrual-maps/tvcg-2018-shadowaccrualmaps.pdf):

**Shadow Accrual Maps: Efficient Accumulation of City-Scale Shadows over Time**   
[Fabio Miranda](https://fmiranda.me), [Harish Doraiswamy](https://harishd.com/), [Marcos Lage](http://www2.ic.uff.br/~mlage), Luc Wilson, Mondrian Hsieh, [Claudio T. Silva](https://vgc.poly.edu/~csilva)  
*IEEE Transactions on Visualization and Computer Graphics, vol. 25, no. 3, pp. 1559-1574, Mar 2019*

Citation:
```
@ARTICLE{8283638,
author={F. Miranda and H. Doraiswamy and M. Lage and L. Wilson and M. Hsieh and C. T. Silva},
journal={IEEE Transactions on Visualization and Computer Graphics},
title={Shadow Accrual Maps: Efficient Accumulation of City-Scale Shadows Over Time},
year={2019},
volume={25},
number={3},
pages={1559-1574},
keywords={Urban areas;Ray tracing;Buildings;Visual analytics;Sun;Tools;Shadow accumulation;shadow accrual maps;visual analysis;urban development},
doi={10.1109/TVCG.2018.2802945},
ISSN={1077-2626},
month={March}}

```

Shadow Accrual Maps has been feature on [The New York Times](https://www.nytimes.com/interactive/2016/12/21/upshot/Mapping-the-Shadows-of-New-York-City.html), together with an interactive visualization of the accumulated shadows in New York City. It has also been feature on [GeoAwesomeness](http://geoawesomeness.com/amazing-map-shows-shadows-new-york-city/), [Technical.ly](https://technical.ly/brooklyn/2016/12/23/building-shadow-map-new-york-times/), among others.

A video is available [here](https://www.youtube.com/watch?v=LsZv23d1LyM).

![Shadow accrual map example](https://raw.githubusercontent.com/ViDA-NYU/shadow-accrual-maps/master/nyc-shadow.png?token=ACRuim7NEAqvjJEStnb0lqb48gFm-_J9ks5cCy20wA%3D%3D)



## Shadow Accumulation Data

![Shadow example](https://raw.githubusercontent.com/ViDA-NYU/shadow-accrual-maps/master/cities.png?token=ACRuim7NEAqvjJEStnb0lqb48gFm-_J9ks5cCy20wA%3D%3D)

The shadow accumulation data can be downloaded through Open Science Framework [here](https://osf.io/4tqp9/), or visualized [here](https://vgc.poly.edu/projects/shadow). We have made available data for:

- New York City
- Chicago (visualizations: [June 21](https://vgc.poly.edu/projects/shadows/?city=chi&day=jun-21), [Sep 22](https://vgc.poly.edu/projects/shadows/?city=chi&day=sep-22), [Dec 21]([Dec 21](https://vgc.poly.edu/projects/shadows/?city=chi&day=dec-21))
- Los Angeles (visualizations: [June 21](https://vgc.poly.edu/projects/shadows/?city=la&day=jun-21), [Sep 22](https://vgc.poly.edu/projects/shadows/?city=la&day=sep-22), [Dec 21]([Dec 21](https://vgc.poly.edu/projects/shadows/?city=la&day=dec-21))
- Washington D.C. (visualizations: [June 21](https://vgc.poly.edu/projects/shadows/?city=dc&day=jun-21), [Sep 22](https://vgc.poly.edu/projects/shadows/?city=dc&day=sep-22), [Dec 21]([Dec 21](https://vgc.poly.edu/projects/shadows/?city=dc&day=dec-21))
- Boston (visualizations: [June 21](https://vgc.poly.edu/projects/shadows/?city=bos&day=jun-21), [Sep 22](https://vgc.poly.edu/projects/shadows/?city=bos&day=sep-22), [Dec 21]([Dec 21](https://vgc.poly.edu/projects/shadows/?city=bos&day=dec-21)))

The accumulated shadows were computed for three days of the year: June 21 (summer solstice), September 22 (autumnal equinox) and December 21 (winter solstice). Shadows can be greatly distorted when they are near the horizon, so all the shadows in the model are estimated from one and a half hours after sunrise to one and a half hours before sunset.

Each tar.gz or zip file contains a folder structure following the slippy tiles hierarchy (see [here](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames)), with both png and binary files; the png files can be visualized over any map that uses slippy tiles (e.g., Google Maps, OpenStreetMap). The binary files contain the raw accumulation values for the considered time ranges. We provide a python script to facilitate the retrieval of shadow values, given a lat/lon as an input. For example:

```
python shadow.py --lat 40.749785 --lon -73.987774 --path ./slippy-nyc-dec-21
```
