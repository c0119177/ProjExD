import pygame as pg
import sys
import random
import numpy as np

maxspeed = 3
#スクリーン用クラス
class Screen:
    def __init__(self, title, wh: tuple, img):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rect = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(img).convert()
        self.bg_rect = self.bg_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rect)

#こうかとん用クラス
class Bird:
    def __init__(self, img, size: float, xy: tuple):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rect = self.sfc.get_rect()
        self.rect.center = xy

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        key = pg.key.get_pressed()
        tori_speed = 1
        if key[pg.K_UP]:
            self.rect.centery -= tori_speed
        if key[pg.K_DOWN]:
            self.rect.centery += tori_speed
        if key[pg.K_LEFT]:
            self.rect.centerx -= tori_speed
        if key[pg.K_RIGHT]:
            self.rect.centerx += tori_speed
        if check_bound(self.rect, screen.rect) != (1, 1):
            if key[pg.K_UP]:
                self.rect.centery += tori_speed
            if key[pg.K_DOWN]:
                self.rect.centery -= tori_speed
            if key[pg.K_LEFT]:
                self.rect.centerx += tori_speed
            if key[pg.K_RIGHT]:
                self.rect.centerx -= tori_speed
        self.blit(screen)


#爆弾用クラス
class Bomb:
    def __init__(self, color: tuple, rad: int, screen: Screen):
        self.sfc = pg.Surface((rad * 2 , rad * 2))
        self.sfc.set_colorkey((0, 0, 0))
        for i in range(4):
            pg.draw.circle(self.sfc, (color[0] - i * color[0] // 4, color[1] - i * color[1] // 4, color[2] - i * color[2] // 4), (rad, rad), rad - i * (rad // 4 + 1))
        self.rect = self.sfc.get_rect()
        self.rect.centerx = random.randint(rad * 2, screen.rect.width - rad * 2)
        self.rect.centery = random.randint(rad * 2, screen.rect.height - rad * 2)
        self.vx = np.random.choice([-1, 1])
        self.vy = np.random.choice([-1, 1])

    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rect)

    def update(self, screen: Screen):
        global maxspeed
        self.rect.move_ip(self.vx, self.vy)
        w, h = check_bound(self.rect, screen.rect)
        maxspeed = 3
        if (w, h) != (1, 1):
            if w == -1:
                if self.vx >= maxspeed:
                    self.vx = 2.5
                if self.vx <= -1 * maxspeed:
                    self.vx = -2.5
                self.vx *= -1
                self.vx += random.uniform(-1, 1)
            if h == -1:
                if self.vy >= maxspeed:
                    self.vy = 2.5
                if self.vy <= -1 * maxspeed:
                    self.vy = -2.5
                self.vy *= -1
                self.vy += random.uniform(-1, 1)
        self.blit(screen)


def main():
    global maxspeed
    #fpsのカウント開始
    clock = pg.time.Clock()
    sc = Screen("負けるな！こうかとん", (1600, 900), "../fig/pg_bg.jpg")
    tori = Bird("../fig/6.png", 2.0, (900, 400))
    bomb = Bomb((255, 0, 0), 50, sc)

    #描画
    while True:
        sc.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return


        tori.update(sc)
        bomb.update(sc)

        if tori.rect.colliderect(bomb.rect):
            return
        maxspeed += 0.001
        pg.display.update()
        clock.tick(1000)

def check_bound(rect, sc_rect):
    w, h = 1, 1
    if rect.left < sc_rect.left or rect.right > sc_rect.right:
        w = -1
    if rect.top < sc_rect.top or rect.bottom > sc_rect.bottom:
        h = -1
    return w, h


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()