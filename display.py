import pygame
import object
import numericalSolution as ns

colors = [
  # red
  (255, 0, 0),
  # green
  (0, 255, 0),
  # blue
  (0, 0, 255),
  # white
  (255, 255, 255),
  # yellow
  (255, 255, 0),
  # pink
  (255, 0, 255),
  # cyan
  (0, 255, 255),
  # grey
  (127, 127, 127)
]


class Display:
  def __init__(self):
    self.tick = 100
    self.size = 1024
    self.matrix = (self.size, self.size)
    self.caption = "3 Body Simulation"
    self.cursorPosition = None
    self.objects = []
    self.bodyLimit = 3
    self.clear()
    self.window = pygame.display.set_mode(self.matrix)
    self.solver = ns.Solver()

  def clear(self):
    self.radius = 50
    self.color = (255, 0, 0, 50)
    self.colorIndex = 0
    self.density = 100
    self.velocity = [0, 0]
    self.acceleration = [0, 0]

  def keyHandler(self, key):
    if key == '+':
      self.radius += 5
    elif key == '-':
      self.radius -= 5
    elif key == 'c':
      self.colorIndex += 1
      if self.colorIndex > 7:
        self.colorIndex = 0
    elif key == 'C':
      self.colorIndex -= 1
      if self.colorIndex < 0:
        self.colorIndex = 7
    elif key == 'd':
      self.density += 50
    elif key == 'D':
      self.density -= 50
      if self.density < 0:
        self.density = 0
    elif key == 'v':
      self.velocity[0] += 10
      self.velocity[1] += 10
    elif key == 'V':
      self.velocity[0] -= 10
      self.velocity[1] -= 10
    elif key == 'x':
      self.velocity[0] += 10
    elif key == 'X':
      self.velocity[0] -= 10
    elif key == 'y':
      self.velocity[1] += 10
    elif key == 'Y':
      self.velocity[1] -= 10
    self.color = colors[self.colorIndex]

  def eventHandler(self, event, keys):
    if event.type == pygame.MOUSEBUTTONDOWN:
      obj = object.Object(self.cursorPosition, self.radius, self.color, self.density, tuple(self.velocity), tuple(self.acceleration))
      self.objects.append(obj)
      if len(self.objects) > self.bodyLimit:
        self.objects.pop(0)
      self.clear()
    elif event.type == pygame.KEYDOWN:
      self.keyHandler(event.unicode)

  def drawUnderCursor(self):
    self.cursorPosition = pygame.mouse.get_pos()
    pygame.draw.circle(self.window, self.color,
                       self.cursorPosition, self.radius)

  def drawEntities(self):
    self.drawUnderCursor()
    for obj in self.objects:
      obj.updateAcceleration()
      obj.updateVelocity()
      obj.updatePosition()
      pygame.draw.circle(self.window, obj.color, [int(x) for x in obj.pos],
                         obj.radius)

  def run(self):
    pygame.display.set_caption(self.caption)
    run = True
    while run:
      pygame.time.delay(self.tick)
      self.window.fill((0, 0, 0, 150))
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        keys = pygame.key.get_pressed()
        self.eventHandler(event, keys)
      self.solver.solve(self.objects)
      self.drawEntities()
      pygame.display.update()


if __name__ == "__main__":
  display = Display()
  display.run()
