from turtle import Screen
import pygame as pg
import sys

from pyparsing import White

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    Screen_sfc = pg.display.set_mode((1600, 900))
    Screen_rect = Screen_sfc.get_rect()
    bgimg_sfc = pg.image.load("../fig/pg_bg.jpg")
    bgimg_rect = bgimg_sfc.get_rect()
#    Screen_sfc.blit(bgimg_sfc, bgimg_rect)

    tori_sfc = pg.image.load("../fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rect = tori_sfc.get_rect()
    tori_rect.center = 900, 400

    while True:
        Screen_sfc.blit(bgimg_sfc, bgimg_rect)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        key = pg.key.get_pressed()

        if key[pg.K_UP] == True:
            tori_rect.centery -= 1
        if key[pg.K_DOWN] == True:
            tori_rect.centery += 1
        if key[pg.K_LEFT] == True:
            tori_rect.centerx -= 1
        if key[pg.K_RIGHT] == True:
            tori_rect.centerx += 1

        Screen_sfc.blit(tori_sfc, tori_rect)
            
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()