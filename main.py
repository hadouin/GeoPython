# Project setup

import pygame as pg
import random
from os import path 
from settings import *
from sprites import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'testlvlmap.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):
        # start a new game
        #groups
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.all_objects = pg.sprite.Group()
        #player
        self.player = Player(self, 3, 8)
        self.all_sprites.add(self.player)
        #ground
        self.ground = Platform(self, 0, 9, 20, 1)
        #platforms
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Platform(self, col, row, 1, 1)
                    print('plat created')
                if tile == '2':
                    Spike(self,col,row)
        #do not delete :
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        #test collision avec les plateformes
        hits_platform = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits_platform:
            print(hits_platform[0].rect)
            print(hits_platform[0].rect.top)
            if self.player.vel.y > 0 and self.player.pos.y < hits_platform[0].rect.top + (self.player.acc.y / 2) + self.player.vel.y + 1:
                self.player.pos.y = hits_platform[0].rect.top + 0.5
                self.player.vel.y = 0
            else:
                self.player.kill()
                self.playing = False
        #test collision avec les pics

        #move 'camera'
        for plat in self.all_objects:
            plat.rect.x -= GAME_SPEED
        self.ground.rect.x += GAME_SPEED

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            #check for jump
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game Loop - draw
        self.screen.fill(DARKGREY)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        pass

    def show_go_screen(self):
            pass


g = Game()
g.show_start_screen()
g.load_data()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
