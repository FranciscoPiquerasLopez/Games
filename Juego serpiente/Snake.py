import pygame

class Snake:
    def __init__(self, x, y, size):
        self.size = size
        self.body = [(x, y)]

    def move(self, direction, speed):
        x, y = self.body[0]
        if direction == 'UP':
            y -= speed
            if(y < 0):
                y = 400
        elif direction == 'DOWN':
            y += speed
            if(y > 400):
                y = 0
        elif direction == 'LEFT':
            x -= speed
            if(x < 0):
                x = 600
        elif direction == 'RIGHT':
            x += speed
            if(x > 600):
                x = 0
        self.body.insert(0, (x, y))
        self.body.pop()

    def draw(self, screen):
        for pos in self.body:
            pygame.draw.rect(screen, "GREEN", (pos[0], pos[1], self.size, self.size))

    def grow(self):
        self.body.append(self.body[-1])