#!/usr/bin/python
#
# UV sphere mesh experiment
# reference:
#   https://github.com/zhongyn/opengl-8-ball-pool-game
#
# also:
#   https://gamedevdaily.io/four-ways-to-create-a-mesh-for-a-sphere-d7956b825db4#.jgbu4qs54
# 
#   for j in parallels_count:
#    parallel = PI * (j+1) / parallels_count  # GN: +1 offset is arbitrary?
#     for i in meridians_count:
#       meridian = 2.0 * PI * i / meridians_count
#       return spherical_to_cartesian(meridian, parallel)
#
import math

PI = math.pi  # 3.14159



def makeSphereVertices(radius, slices, stacks):


  parallels_count =  stacks
  meridians_count =  slices

  stepsk = PI / parallels_count
  stepsl = 2 * PI / meridians_count

  for i in range(parallels_count):

    thetaR =      0  + (i * PI / parallels_count)  #  Z
#    thetaR =  -PI/2  + (i * PI / parallels_count)  # G

    rlat = math.cos(thetaR)    # circle radius at this parallel

    print "theta = %fd (%.3fr)  [R=%.3f]" % (thetaR * 180.0/PI, thetaR, rlat)

    for j in range(meridians_count):

      phi = j * 2.0 * PI / meridians_count  # angle in radians from circumference of unit circle 

      print "  v(%2d) [%7.4f] " % (i*parallels_count+j, phi)

      # first point
      ex =  math.sin(thetaR) * math.sin(phi)
      ey =  math.cos(thetaR)
      ez = math.sin(thetaR) * math.cos(phi)

      tx = -(-math.atan2(ex, ey) / PI + 1.0) / 2
      ty = -math.acos(ez) / PI

      # second point
      ex = (math.sin(thetaR + stepsk) * math.sin(phi))
      ey =  math.cos(thetaR + stepsk)
      ez = (math.sin(thetaR + stepsk) * math.cos(phi))

      tx = -(-math.atan2(ex, ey) / PI + 1.0) / 2
      ty = -math.acos(ez) / PI


      #vec3 = z_spherical_to_cartesian(phi, thetaR)

      #print "  v(%2d) [%7.4f] [%7.3f, %7.3f, %7.3f]" % (i*parallels_count+j, phi, 
      #    vec3[0], vec3[1], vec3[2])



# zhongyaonan method
def z_spherical_to_cartesian(phi, thetaR):

  # glm::vec3 v1 = glm::vec3(sin(theta) * sin(phi), cos(theta), sin(theta) * cos(phi));
  # glm::vec3 v2 = glm::vec3(sin(theta + stepsk) * sin(phi), cos(theta + stepsk), sin(theta + stepsk) * cos(phi));
  x = math.sin(thetaR) * math.sin(phi)      
  y = math.cos(thetaR)
  z = rlat * math.cos(phi)
  vec3 = [x, y, z]

  return vec3

# my method
def g_spherical_to_cartesian(phi, thetaR):

#  thetaR -=  PI / 2 

  r = math.cos(thetaR)  # circle radius at this parallel
  x = r * math.cos(phi)      
  y = math.sin(thetaR)
  z = r * math.sin(phi)
  vec3 = [x, y, z]

  return vec3
  
  
def main():
#  radius = int(input("circle radius? "))
  radius = 1.0
  slices = 8
  stacks = 4
  #      mStrips = divide / 2;
  #      mStripePointsNum = (divide + 1) * 2;
  makeSphereVertices(radius, slices, stacks)
    

main()  


