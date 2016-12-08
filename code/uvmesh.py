#!/usr/bin/python
#
# UV sphere mesh experiment
# reference:
#   https://gamedevdaily.io/four-ways-to-create-a-mesh-for-a-sphere-d7956b825db4#.jgbu4qs54
#
#   https://github.com/zhongyn/opengl-8-ball-pool-game
#
import math

PI = 3.14159

def main():
#  radius = int(input("circle radius? "))
#  PI = 3.14159
  r = 1  # radius ... unit circle

  parallels_count =  int(input("parallels_count? "))
  meridians_count =  int(input("meridians_count? "))

  for i in range(parallels_count):

    #thetaR = PI * (i+1) / parallels_count    # GN: why +1 ?
    thetaR = (i * PI / parallels_count) #  - (PI/2)

    print "theta = %fd %.3fr  (R=%.3f)" % (thetaR * 180.0/PI, thetaR, math.cos(thetaR))

    for j in range(meridians_count):

      phi = j * 2.0 * PI / meridians_count  # angle in radians from circumference of unit circle 

      vec3 = g_spherical_to_cartesian(phi, thetaR)

      print "  v(%d) [%.4f] [%0.3f, %0.3f, %0.3f]" % (i*parallels_count+j, phi, 
          vec3[0], vec3[1], vec3[2])

# zhongyaonan method
def z_spherical_to_cartesian(phi, thetaR):

  rlat = math.sin(thetaR)  # circle radius at this parallel
  x = rlat * math.sin(phi)      
  y = math.cos(thetaR)
  z = rlat * math.cos(phi)
  vec3 = [x, y, z]

  return vec3

# my method
def g_spherical_to_cartesian(phi, thetaR):
  thetaR -=  PI / 2 
  rlat = math.cos(thetaR)  # circle radius at this parallel
  x = rlat * math.cos(phi)      
  y = math.sin(thetaR)
  z = rlat * math.sin(phi)
  vec3 = [x, y, z]

  return vec3
  

main()  
