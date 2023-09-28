import pygame

pygame.init()
game = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

balls = []

upHeld = False
downHeld = False
leftHeld = False
rightHeld = False

class Ball():
    def __init__(self,x,y,size):
        self.x = x
        self.xv = 0
        self.y = y
        self.yv = 0
        self.size = size
        
    def update(self):
        self.x += self.xv
        self.y += self.yv
    def tick(self):
        if self.xv > 0:
            self.xv -= 1
        if self.xv < 0:
            self.xv += 1
        if self.yv > 0:
            self.yv -= 1
        if self.yv < 0:
            self.yv += 1
        
        
    def show(self):
        pygame.draw.circle(game, white, (self.x,self.y), self.size)

while True:
    game.fill(black)
    for ball in balls:
        if abs(ball.yv)<10:
            if downHeld:
                ball.yv += 2
            if upHeld:
                ball.yv -= 2
        if abs(ball.xv)<10:
            if leftHeld:
                ball.xv -= 2
            if rightHeld:
                ball.xv += 2
        ball.tick()
        ball.update()
        ball.show()
    pygame.display.update()
    for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_w:
                          upHeld = True
                      if event.key == pygame.K_s:
                          downHeld = True
                      if event.key == pygame.K_a:
                          leftHeld = True
                      if event.key == pygame.K_d:
                          rightHeld = True
                  if event.type == pygame.KEYUP:
                      if event.key == pygame.K_w:
                          upHeld = False
                      if event.key == pygame.K_s:
                          downHeld = False
                      if event.key == pygame.K_a:
                          leftHeld = False
                      if event.key == pygame.K_d:
                          rightHeld = False

                          
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      mx,my = pygame.mouse.get_pos()
                      balls.append(Ball(mx,my,50))
    clock.tick(60)
                      
    
        
