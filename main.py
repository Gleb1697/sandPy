import sys
import pygame

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
SIZEX = 800
SIZEY = 600
SIZE = (SIZEX, SIZEY)


pygame.init()


class Game():
    def __init__(self):
        self.movex = 10
        self.movey = 10
        self.rectsizex = 30
        self.rectsizey = 30
        self.rectx = (SIZEX - self.rectsizex) / 2
        self.recty = (SIZEY - self.rectsizey) / 2
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.rectx -= self.movex
                if self.rectx <= 0 :
                    self.rectx = 0
            if keys[pygame.K_RIGHT] :
                self.rectx += self.movex
                if self.rectx >= SIZEX - self.rectsizex :
                    self.rectx = SIZEX - self.rectsizex
            if keys[pygame.K_UP]:
                self.recty -= self.movey
                if self.recty <= 0 :
                    self.recty = 0
            if keys[pygame.K_DOWN]:
                self.recty += self.movey
                if self.recty >= SIZEY - self.rectsizey :
                    self.recty = SIZEY - self.rectsizey
                

            self.screen.fill(WHITE)
            self.rect = [self.rectx, self.recty, self.rectsizex, self.rectsizey]
            pygame.draw.rect(self.screen, BLACK, self.rect)
            pygame.display.flip()


Game().run()
