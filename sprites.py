# Sprite Classes
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.pos = vec(x * TILESIZE + (TILESIZE / 2),
                       y * TILESIZE + (TILESIZE / 2))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms, False) # test si touche plateforme
        self.rect.x -= 1 
        if hits:
            self.vel.y = JUMPFORCE

    def update(self):
        self.acc = vec(0, PLAYER_ACC)
        # friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations du mouvement
        self.vel += self.acc 
        self.pos += self.vel + 0.5 * self.acc
        # positionnement
        self.rect.midbottom = self.pos
        # self.mask = pg.mask.from_surface(self.image)

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.all_sprites, game.platforms, game.all_objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((w * TILESIZE, h * TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Spike(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.spikes, game.all_objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("spike02.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.mask = pg.mask.from_surface(self.image)

class Jump_Pad(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.jumpPads, game.all_objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE * 1 / 10))
        self.image.fill(LIGHTBLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE 
        self.rect.y = y * TILESIZE + TILESIZE * 9 / 10
        