import sys
from gui import *
import pygame

pygame.init()


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((1200,700))
        self.clock = pygame.time.Clock()
        self.GUI = GUI()





    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()


            self.screen.fill((0,0,0))
            self.GUI.draw(self.screen)


            pygame.display.flip()
            self.clock.tick(60)


    def quit(self):
        sys.exit()
        pygame.quit()




if __name__ == '__main__':
    App().run()