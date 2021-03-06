import pygame as pg
import sys
import random
import numpy as np

from pyparsing import White

def main():
    #fpsのカウント開始
    clock = pg.time.Clock()
    #スクリーン設定
    pg.display.set_caption("逃げろ！こうかとん")
    Screen_sfc = pg.display.set_mode((1600, 900))
    Screen_rect = Screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("../fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
    #こうかとん設定
    tori_sfc = pg.image.load("../fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center = 900, 400
    #爆弾設定
    bomb_sfc = pg.Surface((100, 100))
    bomb_sfc.set_colorkey((0, 0, 0))
    for i in range(4):
        pg.draw.circle(bomb_sfc, (255 - i * 63, 0, 0), (50, 50), 50 - i * 10)
    bomb_rect = bomb_sfc.get_rect()
    bomb_rect.centerx = random.randint(100, Screen_rect.width - 100)
    bomb_rect.centery = random.randint(100, Screen_rect.height - 100)

    vx = np.random.choice([-1, 1])
    vy = np.random.choice([-1, 1])

    #描画
    while True:
        Screen_sfc.blit(bgimg_sfc, bgimg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key = pg.key.get_pressed()
        tori_speed = 1

        #こうかとん移動関連
        if key[pg.K_UP] == True:
            tori_rect.centery -= tori_speed
        if key[pg.K_DOWN] == True:
            tori_rect.centery += tori_speed
        if key[pg.K_LEFT] == True:
            tori_rect.centerx -= tori_speed
        if key[pg.K_RIGHT] == True:
            tori_rect.centerx += tori_speed
        if check_bound(tori_rect, Screen_rect) != (1, 1):
            if key[pg.K_UP] == True:
                tori_rect.centery += tori_speed
            if key[pg.K_DOWN] == True:
                tori_rect.centery -= tori_speed
            if key[pg.K_LEFT] == True:
                tori_rect.centerx += tori_speed
            if key[pg.K_RIGHT] == True:
                tori_rect.centerx -= tori_speed


        Screen_sfc.blit(tori_sfc, tori_rect)

        Screen_sfc.blit(bomb_sfc, bomb_rect)

        #爆弾の反射
        bomb_rect.move_ip(vx, vy)
        w, h = check_bound(bomb_rect, Screen_rect)
        if (w, h) != (1, 1):
            if w == -1:
                if vx >= 3.5:
                    vx = 3
                if vx <= -3.5:
                    vx = -3
                vx *= -1
                vx += random.uniform(-1, 1)
            if h == -1:
                if vy >= 3.5:
                    vy = 3
                if vy <= -4:
                    vy = -3
                vy *= -1
                vy += random.uniform(-1, 1)

        if tori_rect.colliderect(bomb_rect):
            return
                        
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