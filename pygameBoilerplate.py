import pygame
import random
import math
width = 700
height = 700
UP = -1
DOWN = 1
LEFT = -1
RIGHT = 1
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
GRAVITY = 10
pygame.init()
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.mixer.init()

class Ball:
    
    def __init__(self):
        self.y = width / 2
        self.x = height / 2
        self.c = RED
        self.r = 20

    def draw(self):
        pygame.draw.circle(screen, self.c, (int(self.x), int(self.y)), self.r)

class Audio:
    def __init__(self):
        #self.ballBreak = pygame.mixer.Sound("ballBreak.wav")
        pass
    def playBallBreak(self):
        #self.ballBreak.play()
        pass

   
def circleOverlap(c1, c2):
    return math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2) < c1.r + c2.r

def squareOverlap(s1, s2):
    if (s1.x < s2.x + s2.w and s1.x > s2.x - s2.w) and s1.y < s2.y + s2.h and s1.y > s2.y - s2.h:
        return True
    return False
           
            
         
def main():
    done = False
    ball = Ball()
    while not done:
        pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
##            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:

        
           
        #x, y = pygame.mouse.get_pos()
        #print(x, y)
        
        ball.draw()
        pygame.display.flip()
        clock.tick(60)
        screen.fill((0, 0, 0))
        
        
    pygame.display.quit()
    pygame.quit()
    
main()
