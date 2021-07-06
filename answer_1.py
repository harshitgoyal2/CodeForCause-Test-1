from math import pi,pow # get value of pi and pow function from math module

# get radius from user
radius = float(input("Enter the radius of the circle: "))
# calculate area of circle 
area = float(pi * pow(radius,2))
# printing area of circle
print(area)
# print area of circle upto 3 decimal
print("{:.3f}".format(area))