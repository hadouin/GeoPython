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
        self.icon = pg.image.load(ICON)
        pg.display.set_icon(self.icon)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT)
        self.running = True

    def load_data(self): # Mets la Map dans le tableau
        game_folder = path.dirname(__file__)
        self.map_data = [[],[]]
        with open(path.join(game_folder, 'testlvlmap.txt'), 'rt') as f:
            for line in f:
                self.map_data[0].append(line)
        with open(path.join(game_folder, 'MAP.txt'), 'rt') as f:
            for line in f:
                self.map_data[1].append(line)        

    def new(self):
        # start a new game
        #groups
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.all_objects = pg.sprite.Group()
        self.jumpPads = pg.sprite.Group()
        self.Orbs = pg.sprite.Group()
        #player
        self.player = Player(self, 3, 8)
        #ground
        self.ground = Platform(self, 0, 9, 20, 1)
        #platforms / parcourir le tableau de la map et tout afficher
        for row, tiles in enumerate(self.map_data[self.MapNumber]):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Platform(self, col, row, 1, 1)
                    # print('plat created')
                if tile == '2':
                    Spike(self, col, row)
                if tile == '3':
                    Jump_Pad(self, col, row)
                if tile == '4':
                    Orbs(self, col, row)
        #do not delete :
        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        self.GameOver = False
        self.space_down = False
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        # add 'kill all sprites'

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        #test collision avec les plateformes
        hits_platform = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits_platform:
            if self.player.vel.y > 0 and self.player.pos.y < hits_platform[0].rect.top + (self.player.acc.y / 2) + self.player.vel.y + 1:
                self.player.pos.y = hits_platform[0].rect.top + 0.5
                self.player.vel.y = 0
            else:
                print("Plat hit")
                self.player.kill()
                self.playing = False
                self.GameOver = True
        #test collision avec les pics
        hits_spikes_rect = pg.sprite.spritecollide(self.player, self.spikes, False)
        if hits_spikes_rect:
            print("spike hit")
            self.player.kill()
            self.playing = False
            self.GameOver = True
        #test collision avec les pads de saut
        hits_JumpPad = pg.sprite.spritecollide(self.player, self.jumpPads, False)
        if hits_JumpPad:
            print("jump hit")
            self.player.vel.y = JUMPFORCE
        #move 'camera'
        for plat in self.all_objects:
            plat.rect.x -= GAME_SPEED
        self.ground.rect.x += GAME_SPEED

    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
                self.Level = False
            #check for jump
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.space_down = True
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE: 
                    self.space_down = False
        if self.space_down:
            self.player.jump(self)

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
        self.Start = True
        self.MapNumber = 0
        while self.Start:
            self.screen.fill(DARKGREY)
            self.draw_grid()
            pg.draw.rect(self.screen, LIGHTGREEN, (100, 50, 1000, 500))
            self.draw_text("GéoPython", 30, WHITE, WIDTH / 2, HEIGHT / 4 - 15)
            self.draw_text("<- " + str(self.map_data[self.MapNumber][9]) + " ->", 30, WHITE, WIDTH / 2, HEIGHT / 2 - 15)
            self.draw_text("[Enter] : Jouer", 30, WHITE, WIDTH / 2, HEIGHT * 3 / 4 - 15)
            pg.display.flip()
            for event in pg.event.get():
                self.clock.tick(FPS)
                if event.type == pg.QUIT:
                    self.playing = False
                    self.running = False
                    self.GameOver = False
                    self.Level = False
                    self.Start = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        if self.MapNumber < TOTALMAPS - 1:
                           self.MapNumber += 1
                    if event.key == pg.K_LEFT:
                        if self.MapNumber > 0:
                           self.MapNumber -= 1
                    if event.key == pg.K_RETURN:
                        self.Start = False
                        self.Level = True

    def show_go_screen(self):
        if self.GameOver:
            self.screen.fill(DARKGREY)
            self.draw_grid()
            pg.draw.rect(self.screen, BLUE, (100, 50, 1000, 500))
            self.draw_text("Game Over", 30, WHITE, WIDTH / 2, HEIGHT / 4 - 15)
            self.draw_text("[Esc] : Retour au menu", 30, WHITE, WIDTH / 2, HEIGHT / 2 - 15)
            self.draw_text("[Enter] : Rejouer", 30, WHITE, WIDTH / 2, HEIGHT * 3 / 4 - 15)
            pg.display.flip()
            while self.GameOver:
                for event in pg.event.get():
                    self.clock.tick(FPS)
                    if event.type == pg.QUIT:
                        self.playing = False
                        self.running = False
                        self.GameOver = False
                        self.Level = False
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_ESCAPE:
                            self.playing = False
                            self.GameOver = False
                            self.Level = False
                        if event.key == pg.K_RETURN:
                            self.GameOver = False

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.load_data()
while g.running:
    g.show_start_screen()
    while g.Level:
        g.new()
        g.show_go_screen()
pg.quit()
