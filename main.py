import pygame
import os
import Ball
import math
import random
import Holes
import time

#Practice hole for assignment

#window parameters
WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Golf Game (Practice Hole)!")

#RGB colours
WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 180, 0, 0
YELLOW = 255, 255, 0
BLUE = 10, 100, 200
BROWN = 150, 75, 0
GREEN = 0,180,0

#Frames per second
FPS = 50

#Use border as the ground for collision
BORDER = pygame.Rect(0, 495, 900, 5)
#BIG hole to consume golf ball
GREEN_PAD = pygame.Rect(700,175,200,10)
GREEN_UNDERLINE = pygame.Rect(700,183,210,3)
HOLE = pygame.Rect(835, 175, 25, 5)
WALL = pygame.Rect(WIDTH//2 - 5, 400, 10, 500)
TEE_BOX = pygame.Rect(0,495,50,5)

#Green, flag, hazards and skyline parameters
GREEN_WIDTH, GREEN_HEIGHT = 50, 900


FLAG_WIDTH, FLAG_HEIGHT = 50, 60
SKY_WIDTH, SKY_HEIGHT = 900, 500
HAZARD_WIDTH,  HAZARD_HEIGHT = 300,500
SAND_WIDTH, SAND_HEIGHT = 200, 70

GOLF_GREEN = pygame.image.load(os.path.join('Assets', 'green.png'))
GOLF_GREEN = pygame.transform.rotate(
    pygame.transform.scale(GOLF_GREEN, (GREEN_WIDTH, GREEN_HEIGHT)), 270)

GOLF_FLAG = pygame.image.load(os.path.join('Assets', 'flag.png'))
GOLF_FLAG = pygame.transform.rotate(
    pygame.transform.scale(GOLF_FLAG, (FLAG_WIDTH, FLAG_HEIGHT)), 0)

WATER_HAZARD = pygame.image.load(os.path.join('Assets', 'water.png'))
WATER_HAZARD = pygame.transform.rotate(
    pygame.transform.scale(WATER_HAZARD, (HAZARD_WIDTH, HAZARD_HEIGHT)), 0)

SAND_HAZARD = pygame.image.load(os.path.join('Assets', 'sand.png'))
SAND_HAZARD = pygame.transform.rotate(
    pygame.transform.scale(SAND_HAZARD, (SAND_WIDTH, SAND_HEIGHT)), 0)




global SKY
SKY = pygame.image.load(os.path.join('Assets', 'back.png'))
SKY = pygame.transform.rotate(
    pygame.transform.scale(SKY, (SKY_WIDTH, SKY_HEIGHT)), 0)


global DESSERT_SKY
DESSERT_SKY = pygame.image.load(os.path.join('Assets', 'Dessert.png'))
DESSERT_SKY = pygame.transform.rotate(
    pygame.transform.scale(DESSERT_SKY, (SKY_WIDTH, SKY_HEIGHT)), 0)

BLUE_SKY = pygame.image.load(os.path.join('Assets', 'BlueSky.png'))
BLUE_SKY = pygame.transform.rotate(
    pygame.transform.scale(BLUE_SKY, (SKY_WIDTH, SKY_HEIGHT)), 0)



# detects if ball lands in water hazard
WATER_GHOST = pygame.Rect(200, 450, 300, HAZARD_HEIGHT)
SAND_GHOST = pygame.Rect(WIDTH/2-100, HEIGHT/2+50,SAND_WIDTH,SAND_HEIGHT)
BHOLE_GHOST = pygame.Rect(WIDTH/2+255, HEIGHT/2+120,125,125)



# Hole 2 Barriers

H2B = pygame.Rect(WIDTH/2-100, HEIGHT/2+100,200,5)
H2LW = pygame.Rect(WIDTH/2-100,HEIGHT/2+50,5,50)
H2RW = pygame.Rect(WIDTH/2+95,HEIGHT/2+50,5,50)

TREE_LEDGE = pygame.Rect(0,200,165,10)
LEDGE_UNDERLINE = pygame.Rect(0,197,165,3)
LEDGE_UNDERLINE2 = pygame.Rect(0,203,165,3)

#CHRSTMAS UPDATE
TREE_WIDTH, TREE_HEIGHT = 125,175

XMAS_TREE = pygame.image.load(os.path.join('Assets', 'treeX.png'))
XMAS_TREE = pygame.transform.rotate(
    pygame.transform.scale(XMAS_TREE, (TREE_WIDTH, TREE_HEIGHT)), 0)


LIGHT_WIDTH, LIGHT_HEIGHT = 175,25

XMAS_LIGHT = pygame.image.load(os.path.join('Assets', 'lights.png'))
XMAS_LIGHT = pygame.transform.rotate(
    pygame.transform.scale(XMAS_LIGHT, (LIGHT_WIDTH, LIGHT_HEIGHT)), 0)


# BLACKHOLE IMAGES HOLE 2!!!

BHOLE_WIDTH, BHOLE_HEIGHT = 175, 175


blackHole = [
pygame.image.load(os.path.join('black hole png', '1.png')), 
pygame.image.load(os.path.join('black hole png', '2.png')), 
pygame.image.load(os.path.join('black hole png', '3.png')), 
pygame.image.load(os.path.join('black hole png', '4.png')), 
pygame.image.load(os.path.join('black hole png', '5.png')), 
pygame.image.load(os.path.join('black hole png', '6.png')), 
pygame.image.load(os.path.join('black hole png', '7.png')), 
pygame.image.load(os.path.join('black hole png', '8.png')), 
pygame.image.load(os.path.join('black hole png', '9.png')),
pygame.image.load(os.path.join('black hole png', '10.png')),
pygame.image.load(os.path.join('black hole png', '11.png')),
pygame.image.load(os.path.join('black hole png', '12.png')),
pygame.image.load(os.path.join('black hole png', '13.png')),
pygame.image.load(os.path.join('black hole png', '14.png')),
pygame.image.load(os.path.join('black hole png', '15.png')),
pygame.image.load(os.path.join('black hole png', '16.png')),
pygame.image.load(os.path.join('black hole png', '17.png')),]





def hole2():
  global SKY
  #SKY = DESSERT_SKY
  WINDOW.fill(WHITE)
  WINDOW.blit(SKY, (0, 0))
  WINDOW.blit(GOLF_GREEN, (0, 450))
  WINDOW.blit(WATER_HAZARD, (200,450))
  WINDOW.blit(GOLF_FLAG, (845, 125))
  WINDOW.blit(SAND_HAZARD, (WIDTH/2-100, HEIGHT/2+35))
  WINDOW.blit(XMAS_TREE, (WIDTH/2-450, 25))  
  WINDOW.blit(XMAS_LIGHT, (WIDTH/2+260, HEIGHT/2-67))  
  WINDOW.blit(XMAS_LIGHT, (WIDTH/2-460, 207)) 
  

  pygame.draw.rect(WINDOW, BLACK, BORDER)
  pygame.draw.rect(WINDOW, GREEN, GREEN_PAD)
  pygame.draw.rect(WINDOW, WHITE, HOLE)
  pygame.draw.rect(WINDOW, BLACK, H2B)
  pygame.draw.rect(WINDOW, BLACK, H2LW)
  pygame.draw.rect(WINDOW, BLACK, H2RW)
  pygame.draw.rect(WINDOW, BLACK, GREEN_UNDERLINE)
  pygame.draw.rect(WINDOW, GREEN, TEE_BOX)
  pygame.draw.rect(WINDOW, BROWN, TREE_LEDGE)
  pygame.draw.rect(WINDOW, BLACK, LEDGE_UNDERLINE)
  pygame.draw.rect(WINDOW, BLACK, LEDGE_UNDERLINE2)

  
    

  #sand/water ghost for detection (collide point)
  #pygame.draw.rect(WINDOW, BLACK, WATER_GHOST)
  #pygame.draw.rect(WINDOW, BLACK, SAND_GHOST) 
  #pygame.draw.rect(WINDOW, BLACK, BHOLE_GHOST)

  



def hole3():
  pass

def draw_window():
    #hole = Holes.Holes(WINDOW, GOLF_FLAG, SKY, GOLF_GREEN )
    #hole.hole1()
    hole2()
    
    

    golfBall.display(WINDOW)
    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]

    pygame.draw.line(WINDOW, (255, 255, 255), line[0], line[1])


    pygame.display.update()

#def par():
#  currentScore = (STROKE - coursePar)
#  if currentScore 


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    #TextRect.center = screen.get_rect().center
    WINDOW.blit(TextSurf, TextRect)






def fade():
  fade = pygame.Surface((WIDTH,HEIGHT))
  fade.fill((0,0,0))
  for alpha in range(0,300):
    fade.set_alpha(alpha)
    WINDOW.blit(fade,(0,0))
    pygame.display.update()
    pygame.time.delay(1)

def setup():

    global golfBall
    golfBall = Ball.Ball((20, 494), 15)
    golfBall.speed = 0.1
    golfBall.angle = random.uniform(0, math.pi*2) 

    global line
    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]

    global shot
    shot = False




def main():
    setup()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                golfBall.shoot()
            
      

            if HOLE.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("HOLE HIT")
              message_display("In The Hole!")
              time.sleep(2)
              fade()
              hole2()

            #need to lock x-axis to simulate putting
            if GREEN_PAD.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("On Green!")
              message_display("On the Green")
              golfBall.x = golfBall.x

            #re-direct ball
            if TREE_LEDGE.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("OOPS")
            
            #Teleport re-direct onto green
            if BHOLE_GHOST.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("Teleport")
              message_display("Teleport!")
              pygame.time.delay(3)
              fade()
              #green coordinates
              golfBall.x = 720
              golfBall.y = 200
              
            
            if WATER_GHOST.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("Hazard Hit!")
              pygame.time.delay(3)
              message_display("Hazard! +1")
              pygame.time.delay(3)
              fade()
              golfBall.x = 20
              golfBall.y = 494

            #need to make sure ball stays where it lands after hitting image
            if SAND_GHOST.collidepoint(golfBall.x, golfBall.y + golfBall.size):
              print("Hazard Hit!")
              time.sleep(2)
              message_display("SAND")
              fade()

                

        draw_window()
        golfBall.move()
        golfBall.bounce()
        golfBall.display(WINDOW)
        

    pygame.quit()


if __name__ == "__main__":
    main()
