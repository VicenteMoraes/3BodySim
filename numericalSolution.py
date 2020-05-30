class Solver:
  def __init__(self):
    # Gravitational Constant
    self.G = 0.01

  def euclidean(self, A, B):
    return ((A.x - B.x) ** 2 + (A.y - B.y) ** 2) ** 0.5

  def gravity(self, A, B):
    return -self.G * A.mass * B.mass / (self.euclidean(A, B) ** 2)

  def solve(self, objects):
    for objA in objects:
      for objB in objects:
        if objA.pos == objB.pos:
          continue
        magnitude = self.gravity(objA, objB)
        norm = self.euclidean(objA, objB)
        direction = [(objA.x - objB.x) / norm, (objA.y - objB.y) / norm]
        Gforce = [magnitude * dir for dir in direction]
        objA.forces = [force + Gforce[i] for i, force in enumerate(objA.forces)]
        #objB.forces = [force - Gforce for force in objB.forces]
