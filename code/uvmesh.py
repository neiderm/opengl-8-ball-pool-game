#!/usr/bin/python

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

  for j in range(parallels_count):
    #parallel = PI * (j+1) / parallels_count
    parallel = PI * (j) / parallels_count    
    print("parallel = ", parallel)
  
    for i in range(meridians_count):
      meridian = 2.0 * PI * i / meridians_count
      print("  meridian = ", meridian)
  # return spherical_to_cartesian(meridian, parallel)


main()  
