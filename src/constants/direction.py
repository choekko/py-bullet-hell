class Direction:
    def __init__(self, x, y, angle = 0):
        self.x = x
        self.y = y
        self.angle = angle

UP = Direction(0, -1, 0)
DOWN = Direction(0, 1, 180)
LEFT = Direction(-1, 0, 90)
RIGHT = Direction(1, 0, 270)

DIRECTION = {
  'UP': UP,
  'DOWN': DOWN,
  'LEFT': LEFT,
  'RIGHT': RIGHT,
}