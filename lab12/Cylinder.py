class Cyclinder:
  def __init__(self,height,radius):
    self.height = height
    self.radius = radius
  
  def getHeight(self):
    return self.height
  
  def setHeight(self,height):
    if height > 0:
      self.height = height
  
  def getRadius(self):
    return self.radius

  def setRadius(self,radius):
    if radius > 0:
      self.radius = radius
  
  def area(self):
    pi = 3.14
    area_cal = 2*(pi*(self.radius)**2) + 2*pi*self.radius*self.height
    return area_cal

  def volume(self):
    pi = 3.14
    volume_cal = (pi*(self.radius)**2)*self.height
    return volume_cal


cylinder1 = Cyclinder(5,3)

print(cylinder1.area())
print(cylinder1.volume())