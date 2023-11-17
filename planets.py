import pygame, math

pygame.init()
clock = pygame.time.Clock()
game = pygame.display.set_mode((800,800))

g = 10

class Planet():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def blit(self):
        pygame.draw.circle(game,(0,0,0),(self.x,self.y),25)

class Astroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xv = 0
        self.yv = 0

    def pull(self, planet):
        d = math.sqrt(((self.x - planet.x)^2)+((self.y - planet.y)^2))
        
        if d == 0:
            d = 0.01
            
        gStr = g*(1/(d^2))

        y = self.y - planet.y
        x = self.x - planet.x
        
        sin = x/d
        cos = y/d

        dy = y*cos
        dx = x*cos

        self.xv += dx
        self.yv += dy

    def tick(self):
        self.x += self.xv
        self.y += self.yv

    def blit(self):
        pygame.draw.circle(game,(0,0,0),(self.x,self.y),25)
        
        

astroids = []
planets = []
planets.append(Planet(400,400))
astroids.append(Astroid(200,200))

while True:
    for astroid in astroids:
        astroid.tick()
        astroid.blit()
        for planet in planets:
            astroid.pull(planet)
    for planet in planets:
        planet.blit()
    
    
    pygame.display.update()
    clock.tick(60)
