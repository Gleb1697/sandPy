# Import a library of functions called 'pygame'
import pygame
from pygame import KEYDOWN
from math import pi
import sys
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
SIZEX = 400
SIZEY = 300
# Set the height and width of the screen
SIZE = [SIZEX, SIZEY]

class main():
    movex = 10
    movey = 10
    rectsizex = SIZEX/6
    rectsizey = SIZEY/20
    rectx = (SIZEX-rectsizex)/2
    recty = (SIZEY-rectsizey)/2 
    def __init__(self):
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Example code for the draw module")
 
        #Loop until the user clicks the close button.
        done = False
        self.clock = pygame.time.Clock()
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        self.clock.tick(100)
    
    def run(self): 
        while True:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.rectx -=self.movex
                    if event.key == pygame.K_RIGHT:
                        self.rectx +=self.movex
                    if event.key == pygame.K_UP:
                        self.recty -=self.movey
                    if event.key == pygame.K_DOWN:
                        self.recty +=self.movey 
            # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
            self.screen.fill(WHITE)
            self.rect = [self.rectx, self.recty, self.rectsizex, self.rectsizey]
    # Draw a solid rectangle
            pygame.draw.rect(self.screen, BLACK, self.rect)

            pygame.display.flip()
 
# Be IDLE friendly
main().run()