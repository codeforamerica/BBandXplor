import sys
from xml.dom.minidom import parse, parseString

# load the KML file
kml = parse(sys.argv[1])

# print the number of holes
print len( kml.documentElement.getElementsByTagName("innerBoundaryIs") )

# collect only the innerBoundaryIs ( holes )
coords = [ ]
for hole in kml.documentElement.getElementsByTagName("innerBoundaryIs"):
  coords.append( hole.getElementsByTagName("coordinates")[0].toxml() )

# create the new JS file
j = open(sys.argv[2] + ".js", "w")

# output the holes as separate polygons
j.write("function loadHoles(arr){")

for coord in coords:
  mycoord = coord.replace('<coordinates>','').replace('</coordinates>','').split(' ')
  index = 0
  for pt in mycoord:
    pt_array = pt.split(',')
    mycoord[index] = '[' + pt_array[0][0:11] + ',' + pt_array[1][0:10] + ']'
    index = index + 1
  j.write('arr.push([ ' + ','.join(mycoord) + ' ]);')

j.write("}")
j.close()

# create the new KML file
f = open(sys.argv[2] + ".kml", "w")

# output the holes as separate polygons
f.write('''<?xml version="1.0" encoding="utf-8" ?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document><Folder><name>extracttest</name>''')

for coord in coords:
  f.write('<Placemark><MultiGeometry><Polygon><outerBoundaryIs><LinearRing>')
  f.write(coord)
  f.write('</LinearRing></outerBoundaryIs></Polygon></MultiGeometry></Placemark>')

f.write('</Folder></Document></kml>')

f.close()

print "KML file written"
