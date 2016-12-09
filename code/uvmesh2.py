#!/usr/bin/python
#
# UV sphere mesh experiment
# reference:
#   https://github.com/openstreetview/android/blob/master/app/src/main/java/com/telenav/osv/external/glview/model/UVSphere.java
#
import math

PI = 3.14159



def makeSphereVertices(radius, divide, eastSide):
	
  altitude = 0.0
  altitudeDelta = 0.0
  azimuth = 0.0
  ex = 0.0
  ey = 0.0
  ez = 0.0
  startPoint = 0
 

  if eastSide:
     startPoint = 0.0
  else:
     startPoint = math.pi

  for i in range(divide/2):

    altitude =       (math.pi / 2.0 - i       * (math.pi * 2) / divide);
    altitudeDelta =  (math.pi / 2.0 - (i + 1) * (math.pi * 2) / divide);

    vertices  = [0.0] # float[divide * 6 + 6];
    texCoords = [0.0] # float[divide * 4 + 4];			 

#    print "altitude= %f  altitudeDelta= %f" % (altitude, altitudeDelta)
    print "theta = %8.4fd (%.3fr)  [R=%.3f]" % (altitude * 180.0/PI, altitude, math.cos(altitude))
    
    for j in range(divide/2):

      azimuth =  startPoint - (j * (math.pi * 2) / divide) 

      # first point
      ex =  (math.cos(altitudeDelta) * math.cos(azimuth))
      ey =  math.sin(altitudeDelta)
      ez =  (math.cos(altitudeDelta) * math.sin(azimuth))

      vertices.append(radius * ex) # vertices[6 * j + 0] = radius * ex
      vertices.append(radius * ey) # vertices[6 * j + 1] = radius * ey
      vertices.append(radius * ez) # vertices[6 * j + 2] = radius * ez

      texCoords.append(1.0 - (2 * j / divide)) # texCoords[4 * j + 0] = 1.0 - (2 * j /  divide)
      texCoords.append(2 * (i + 1) / divide)   # texCoords[4 * j + 1] = 2 * (i + 1) /  divide

      # second point
      ex =  (math.cos(altitude) * math.cos(azimuth))
      ey =  math.sin(altitude)
      ez =  (math.cos(altitude) * math.sin(azimuth))

      vertices.append(radius * ex) # vertices[6 * j + 3] = radius * ex
      vertices.append(radius * ey) # vertices[6 * j + 4] = radius * ey
      vertices.append(radius * ez) # vertices[6 * j + 5] = radius * ez

      texCoords.append(1.0 - (2 * j / divide)) # texCoords[4 * j + 2] = 1.0 - (2 * j /  divide)
      texCoords.append(2 * i / divide)         # texCoords[4 * j + 3] = 2 * i /  divide

#      print "x0= %7.3f, y0= %7.3f, z0= %7.3f " %  (vertices[6 * j + 0], vertices[6 * j + 1], vertices[6 * j + 2] ) 
      print "x0= %7.3f, y0= %7.3f, z0= %7.3f " %  (vertices[6 * j + 3], vertices[6 * j + 4], vertices[6 * j + 5])
#      print "x0= %7.3f, y0= %7.3f, z0= %7.3f  x1= %7.3f, y1= %7.3f, z1= %7.3f" % \
#                         (vertices[6 * j + 0], vertices[6 * j + 1], vertices[6 * j + 2], 
#                          vertices[6 * j + 3], vertices[6 * j + 4], vertices[6 * j + 5])


def main():

  radius = 1.0
  divide = 8
  eastSide = 1 # true
  makeSphereVertices(radius, divide, eastSide)

 

main()  
