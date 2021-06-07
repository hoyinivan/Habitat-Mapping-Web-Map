"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install --user pyproj

import pyproj

p1 = pyproj.Proj(proj='geocent',ellps='WGS84',datum='WGS84',units='m',no_defs=True)
p2 = pyproj.Proj(init='epsg:4326')

pyproj.transform(p1,p2,-2478053.2006,-3736604.9657,4521684.4805)
(-123.55166435788638, 45.43449642806122, 450.48841851670295)

pyproj.transform(p1,p2,-2393615.9947,5399511.1912,2400677.6139)

with open("M:/FieldTruthingSurvey/Result/Day13_KeungShan/Day13_KeungShan Files/coordinate3.txt", "r") as file:
        for line in file:
            x, y, z = line.split()
            x = float(x)
            y = float(y)
            z = float(z)
            print(pyproj.transform(p1,p2,x,y,z))


