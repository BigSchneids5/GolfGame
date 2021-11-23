import pygame
import random
import math
import numpy as np

background_colour = (255,255,255)
(width, height) = (800, 400)
drag = 0.999
elasticity = 0.75
gravity = (math.pi, 0.002)

def addVectors(a, b):
    x  = math.sin(a[0]) * a[1] + math.sin(b[0]) * b[1]
    y  = math.cos(a[0]) * a[1] + math.cos(b[0]) * b[1]
    
    angle = 0.5 * math.pi - math.atan2(y, x)
    length  = math.hypot(x, y)

    return (angle, length)



class Particle():
    def __init__(self, coords, size):
        self.x = coords[0]
        self.y = coords[1]
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1
        self.speed = 0
        self.angle = 0

    def display(self):
        line = [(particle.x,particle.y),pygame.mouse.get_pos()]
        pygame.draw.line(screen,(0,0,0),line[0],line[1])
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag
        

    def shoot(self):
        vector_1 = pygame.mouse.get_pos()
        vector_2 = (self.x,self.y)
        self.speed = math.dist((self.x,self.y),pygame.mouse.get_pos()) / 400
        
        unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
        unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
        dot_product = np.dot(unit_vector_1, unit_vector_2)

        if vector_1[1] < self.y and vector_1[0] > self.x:
            self.angle = np.arctan(dot_product) 
        elif vector_1[1] < self.y and vector_1[0]< self.x:
            self.angle = np.arctan(dot_product) * -1
        elif vector_1[1] > self.y and vector_1[0] < self.x:
            self.angle = np.arcsin(dot_product) * -1
        elif vector_1[1] > self.y and vector_1[0] > self.x:
            self.angle = np.arcsin(dot_product)
            
        

        self.move()
      

    def bounce(self):
        if self.x > width - self.size:
            self.x = 2*(width - self.size) - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        elif self.x < self.size:
            self.x = 2*self.size - self.x
            self.angle = - self.angle
            self.speed *= elasticity

        if self.y > height - self.size:
            self.y = 2*(height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

        elif self.y < self.size:
            self.y = 2*self.size - self.y
            self.angle = math.pi - self.angle
            self.speed *= elasticity

  
class Path(Particle):
    def __init__(self, coords):
        super(Path, self).__init__(coords, size)
        self.path = []
    
    def display(self):
        for item in self.path:
            pygame.draw.circle(screen, self.colour, (int(item[0]), int(item[1])), self.size, self.thickness)
        

    def move(self):
        (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= drag

        self.path.append((int(self.x),int(self.y)))
        



screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 7')





size = 15
x = random.randint(size, width-size)
y = random.randint(size, height-size)

particle = Particle((x, y), size)
particle.speed = 0.1
particle.angle = random.uniform(0, math.pi*2)




p = Path((particle.x,particle.y))

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            particle.shoot()
            
            p.shoot()
        
 

    screen.fill(background_colour)

    
    particle.move()
    particle.bounce()
    particle.display()
    
    #p.bounce()
    #p.display()
    
    '''     
    positions = []
    my_particles[1].shoot()
    while my_particles[1].y < 381:
        positions.append((my_particles[1].x,my_particles[1].y))
        print(positions)
    for item in positions:
        pygame.draw.circle(screen,(64,64,64),(item[0],item[1]),5,1)
        pygame.display.update()
    print(positions)    
    #'''

    pygame.display.flip()