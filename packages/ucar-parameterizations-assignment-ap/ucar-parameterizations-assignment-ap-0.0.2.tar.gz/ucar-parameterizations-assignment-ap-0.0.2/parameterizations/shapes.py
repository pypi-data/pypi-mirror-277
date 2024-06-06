import math

class Shape:
  def __init__(self, area = 0, perimeter = 0):
    self.area = area
    self.perimeter = perimeter
    
  def calc_volume(self):
    pass
    
  def calc_volume(self):
    pass  

class Sphere(Shape):
  # circumference == perimeter
  def __init__(self, area = 0, perimeter = 0, radius = 0, volume = 0):
    self.area = area
    self.perimeter = perimeter
    self.radius = radius
    self.volume = volume
    
  def calc_perimeter(self, radius = 0):
    # if radius is set by user, ignore object's radius field, otherwise use field
    radius = (self.radius, radius) [radius > 0]
    self.perimeter = 2 * math.pi * radius
    return self.perimeter
  
  def calc_volume(self, radius = 0):
    # if radius is set by user, ignore object's radius field, otherwise use field
    radius = (self.radius, radius) [radius > 0]
    self.volume =  (4 / 3) * math.pi * (radius ** 3) # set volume field
    return self.volume # return value for outside purposes

