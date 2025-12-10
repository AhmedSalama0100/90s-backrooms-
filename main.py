import pygame as pg
import sys
from settings import *
from map import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.clock()

    def new_game(self):
        pass


    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption344(f'{self.clock.get_fps() :.1f}')
    

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


    
    def draw(self):
        self.screen.fill('black')


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
    

if __name__ == '__main__':
    game = Game()
    game.run()
    