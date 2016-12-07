#!/usr/bin/python
#
# UV sphere mesh experiment
# reference:
#   https://gamedevdaily.io/four-ways-to-create-a-mesh-for-a-sphere-d7956b825db4#.jgbu4qs54
#
#   https://github.com/zhongyn/opengl-8-ball-pool-game
#
import math

def main():
  radius = int(input("circle radius? "))
  PI = 3.14159
  r = radius
  c = 2*PI*r
  print("circumf = ", 2*PI*r)
  a = PI*r*r
  print("area = ", PI*r*r)
  ratio = c / a
#  return(ratio)
  print("the ratio of the circumference to the area is",ratio)

  parallels_count =  int(input("parallels_count? "))
  meridians_count =  int(input("meridians_count? "))

  for i in range(parallels_count):
    #thetaR = PI * (i+1) / parallels_count    # GN: why +1 ?
    thetaR = (PI * (i) / parallels_count) - (PI/2)

    
    y = math.sin(thetaR)    # sin(thetaInRadians) gives Y of circle at this parallel     
    rlat = math.cos(thetaR) # cos(thetaInRadians) gives circle radius at this parallel 

    print "theta = %f %.3f  (r=%.3f)" % (thetaR * 180.0/PI, thetaR, rlat)
  
    for j in range(meridians_count):
      phi = 2.0 * PI * j / meridians_count
      x = rlat * math.cos(phi)      
      z = rlat * math.sin(phi)      
      print "  v(%d) [%.4f, %4f] [%0.3f,%0.3f,%0.3f]" % (i*parallels_count+j, phi, thetaR, x, y, z)



  # return spherical_to_cartesian(phi, theta)


main()  
