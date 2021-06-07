A simple web map template (html) for displaying two raster layers in Hong Kong

Recommended pre-processing: 
1. Raster data in GeoTiff format, set to RGB bands and alpha band if necessary
2. Use "Generate XYZ tiles (Directory)" tool in QGIS
3. Put the entire folder in the same location as the html file

Created using Leaflet https://leafletjs.com/examples.html

![habitatmap](https://user-images.githubusercontent.com/68047356/121011596-60201000-c7c9-11eb-95c2-55734e3a0327.png)

Plus a small python script to transform gps coordinates to lat lon height
