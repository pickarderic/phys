import pygame

pygame.init()
game = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

black = (0,0,0)
white = (255,255,255)
orange = (255,165,0)
blue = (0,0,255)

balls = []
walls = []
c1 = (0,0)
c2 = (0,0)

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

    def checkx(self):
        axVal = self.xv
        for wall in self.walls:
            for xvVal in range(0,self.xv):
                tempball = self
                tempball.x += xvVal
                if not allow(wall.x1,wall.y1,wall.x2,wall.y2,[tempball]):
                    if xvVal<axVal:
                        axVal = xvVal
        if axVal == self.xv:
            return (True, axVal)
        return (False,axVal)
    def checky(self):
        ayVal = self.yv
        for wall in self.walls:
            for yvVal in range(0,self.yv):
                tempball = self
                tempball.y += yvVal
                if not allow(wall.x1,wall.y1,wall.x2,wall.y2,[tempball]):
                    if yvVal<ayVal:
                        ayVal = yvVal
        if ayVal == self.yv:
            return (True,ayVal)
        return (False,ayVal)
    
    
    def update(self,walls):
        self.walls = walls
        if not (self.checky())[0]:
            self.y += (self.checky())[1]
        if not (self.checkx())[0]:
            self.x += (self.checkx())[1]
        self.y += self.yv
        self.x += self.xv
        
                
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

class Wall():
    def __init__(self,x1,y1,x2,y2):
        if x2>x1:
            self.width = x2 - x1
        else:
            self.width = x1 - x2
        if x1>x2:
            self.x1 = x2
        else:
            self.x1 = x1
        if y1>y2:
            self.y1 = y2
        else:
            self.y1 = y1
        if y2>y1:
            self.height = y2 - y1
        else:
            self.height = y1 - y2
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
            
    def show(self):
        pygame.draw.rect(game, white, (self.x1, self.y1, self.width, self.height))
        
def isinwall(x,y,wall):
    if wall.x1 <= x and wall.x2 >= x:
        if wall.y1 <= y and wall.y2 >= y:
            return True
    return False

def isincircle(x,y,ball):
    if ((x-ball.x)**2)+((y-ball.y)**2) < ball.size**2:
        return True
    return False

def allow(x1,y1,x2,y2,balls):
    if x1>x2:
        for x in range(x2,x1):
            for ball in balls:
                if isincircle(x,y1,ball):
                    return False
                if isincircle(x,y2,ball):
                    return False
    else:
        for x in range(x1,x2):
            for ball in balls:
                if isincircle(x,y1,ball):
                    return False
                if isincircle(x,y2,ball):
                    return False
    if y1>y2:
        for y in range(y2,y1):
            for ball in balls:
                if isincircle(y,x1,ball):
                    return False
                if isincircle(y,x2,ball):
                    return False
    else:
        for y in range(y1,y2):
            for ball in balls:
                if isincircle(y,x1,ball):
                    return False
                if isincircle(y,x2,ball):
                    return False
    for ball in balls:
        if x2>x1:
            if ball.x < x2 and ball.x > x1:
                if y2>y1:
                    if ball.y < y2 and ball.y > y1:
                        return False
                else:
                    if ball.y > y2 and ball.y < y1:
                        return False
        else:
            if ball.x > x2 and ball.x < x1:
                if y2>y1:
                    if ball.y < y2 and ball.y > y1:
                        return False
                else:
                    if ball.y > y2 and ball.y < y1:
                        return False
                
    return True
                
while True:
    game.fill(black)
    pygame.draw.circle(game, orange, c1, 5)
    pygame.draw.circle(game, orange, c2, 5)
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
        ball.update(walls)
        ball.show()
    for wall in walls:
        wall.show()
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
                      if event.key == pygame.K_x:
                          rx1,ry1 = pygame.mouse.get_pos()
                          c1 = (rx1,ry1)
                      if event.key == pygame.K_c:
                          rx2,ry2 = pygame.mouse.get_pos()
                          c2 = (rx2,ry2)
                      if event.key == pygame.K_z:
                          try:
                              if allow(rx1,ry1,rx2,ry2,balls):
                                  walls.append(Wall(rx1,ry1,rx2,ry2))
                          except:
                              pass
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
                      
    
        
