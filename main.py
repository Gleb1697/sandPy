import sys
import pygame
import map

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
        self.rectsizex = 40
        self.rectsizey = 40
        self.rectx = (SIZEX - self.rectsizex) / 2
        self.recty = (SIZEY - self.rectsizey) / 2
        self.screen = pygame.display.set_mode(SIZE)
        self.player_height = 1
        self.player_width = 1
        self.screen_height = 40
        self.screen_width = 40
        self._bitmap = []
        self.maprectx = SIZEX / self.screen_width
        self.maprecty = SIZEY / self.screen_height
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()

    def run(self):
        self._bitmap = map.Map(self.player_height, self.player_width, self.screen_height, self.screen_width).generate()
        while True:
            self.clock.tick(60)
            self.control_character()
            self.screen.fill(WHITE)
            self.draw_map()
            self.draw_character()
            pygame.display.flip()

    def control_character(self):
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
    
    def draw_map(self):
        a = 0
        for j in self._bitmap:
            b = 0
            for i in j:
                rect = [a, b, self.maprectx, self.maprecty]
                if i == 0:
                    pygame.draw.rect(self.screen, BLACK, rect)
                else:
                    pygame.draw.rect(self.screen, RED, rect)
                b += self.maprecty
            a += self.maprectx
    def draw_character(self):
        rect = [self.rectx, self.recty, self.rectsizex, self.rectsizey]
        pygame.draw.rect(self.screen, BLACK, rect)


    



Game().run()
