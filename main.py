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
movex = 10
movey = 10
rectsizex = SIZEX/6
rectsizey = SIZEY/20
rectx = (SIZEX-rectsizex)/2
recty = (SIZEY-rectsizey)/2 
# Set the height and width of the screen
SIZE = [SIZEX, SIZEY]

class main():
    
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
        global rectx
        global recty
        global rectsizex
        global rectsizey
        while True:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        rectx -=movex
                    if event.key == pygame.K_RIGHT:
                        rectx +=movex
                    if event.key == pygame.K_UP:
                        recty -=movey
                    if event.key == pygame.K_DOWN:
                        recty +=movey 
            # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
            self.screen.fill(WHITE)
            self.rect = [rectx, recty, rectsizex, rectsizey]
    # Draw a solid rectangle
            pygame.draw.rect(self.screen, BLACK, self.rect)

            pygame.display.flip()
 
# Be IDLE friendly
main().run()