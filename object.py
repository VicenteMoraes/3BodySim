from math import pi

class Object:
  def __init__(self, pos, radius, color, density, velocity, acceleration):
    self.pos = pos
    self.radius = radius
    self.color = color
    self.x = pos[0]
    self.y = pos[1]
    self.density = density
    self.area = pi * radius ** 2
    self.mass = self.area * self.density
    self.velocity = velocity
    self.acceleration = acceleration
    self.forces = [0, 0]

  def updateAcceleration(self):
    self.acceleration = [force / self.mass for force in self.forces]

  def update(self, A, B):
    element = list(A)
    increment = list(B)
    return tuple([element[x] + increment[x] for x in range(len(element))])

  def updateVelocity(self):
    self.velocity = self.update(self.velocity, self.acceleration)

  def updatePosition(self):
    self.pos = self.update(self.pos, self.velocity)
