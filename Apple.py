import random

class apple():
    def __init__(self, x, y):
        self.x = int(random.random() * x)
        self.y = int(random.random() * y)

