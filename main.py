import pygame as pg
from classes import Game
# from debug import output
pg.init()

win_rect = pg.Rect((0, 0), (1000, 800))
win = pg.display.set_mode(win_rect.size)
pg.display.set_caption('Up and Over')
pg.display.set_icon(pg.image.load('resources/icon.png'))

clock = pg.time.Clock()
FPS = 60
game = Game()
black_screen = pg.Surface(win.get_size()).convert_alpha()
black_screen.fill('black')


def run():
    while True:
        clock.tick(FPS)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                exit()
        # key_pressed = pg.key.get_pressed()
        # if key_pressed[pg.K_r]:
        #     game.state = 'restarting'
        game.check_scroll_need()
        game.update_objects()
        game.update_height()
        win.fill('lightskyblue1')
        # game.draw_tiles(win)
        game.draw_objects(win)
        handle_game_state()
        pg.display.update()


def handle_game_state():
    if game.state == 'running' and game.player.rect.top > win_rect.bottom:
        game.state = 'restarting'
    if game.state == 'restarting':
        black_screen_alpha = black_screen.get_alpha()
        if black_screen_alpha < 255:
            black_screen_alpha += 10
            black_screen.set_alpha(black_screen_alpha)
            win.blit(black_screen, (0, 0))
        else:
            game.state = 'booting up'
            game.restart()
    if game.state == 'booting up':
        black_screen_alpha = black_screen.get_alpha()
        if black_screen_alpha > 0:
            black_screen_alpha -= 5
            black_screen.set_alpha(black_screen_alpha)
            win.blit(black_screen, (0, 0))
        else:
            game.state = 'running'


if __name__ == "__main__":
    run()
