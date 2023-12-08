import pygame as pg

import gameSetup

# Main Loop
clock = pg.time.Clock()
going = True
while going:
    clock.tick(75)

    # Handle Input Events
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                gameSetup.playerOne.update_account()
                print(gameSetup.playerOne.gold)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()
            mpx = int(mousePos[0] // (500 / gameSetup.SIZE))
            mpy = int(mousePos[1] // (500 / gameSetup.SIZE))
            gameSetup.playerOne.develop_city(mpx, mpy)
            gameSetup.board.get_field(mpx,mpy).update_pop(1)
            # allsprites=pg.sprite.RenderPlain(board[mpx][mpy])
            # allsprites.update()
            gameSetup.screen.blit(gameSetup.board.get_field(mpx,mpy).image, (mpx * gameSetup.FIELD_SIZE, mpy * gameSetup.FIELD_SIZE))
            # allsprites.draw(screen)
            pg.display.flip()
            print(mpx, mpy)
            print(gameSetup.playerOne.Cities[0].gold)
pg.quit()
