import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_flipped = pg.transform.flip(bg_img, True, False)
    kkt_img = pg.image.load("fig/3.png")
    kkt_img = pg.transform.flip(kkt_img, True, False)
    kkt_rct = kkt_img.get_rect()
    kkt_rct.center = 300, 200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed()
        kkt_rct.move_ip(-1 + 2 * key_lst[pg.K_RIGHT] - key_lst[pg.K_LEFT], key_lst[pg.K_DOWN] - key_lst[pg.K_UP])

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_flipped, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kkt_img, kkt_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()