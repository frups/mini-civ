import pygame as pg

import gameSetup

# Main Loop
clock = pg.time.Clock()
going = True
while going:
    clock.tick(75)

    # Handle Input Events
    for event in pg.event.get():
        # User closed windows
        if event.type == pg.QUIT:
            pg.quit()
        # User pressed SPACE button on a keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                gameSetup.playerOne.update_account()
                gameSetup.screen.blit(gameSetup.board.get_field(mpx, mpy).image,
                                      (mpx * gameSetup.FIELD_SIZE, mpy * gameSetup.FIELD_SIZE))
                pg.display.flip()
                print(gameSetup.playerOne.gold)

        # User pressed clicked moose on a field
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousePos = pg.mouse.get_pos()
            mpx = int(mousePos[0] // (500 / gameSetup.NO_FIELDS_PER_ROW))
            mpy = int(mousePos[1] // (500 / gameSetup.NO_FIELDS_PER_ROW))
            gameSetup.playerOne.develop_city(mpx, mpy)
            gameSetup.board.get_field(mpx,mpy).update_pop(1)
            gameSetup.screen.blit(gameSetup.board.get_field(mpx,mpy).image, (mpx * gameSetup.FIELD_SIZE, mpy * gameSetup.FIELD_SIZE))
            pg.display.flip()
            print(mpx, mpy)
            print(gameSetup.playerOne.Cities[0].gold)
pg.quit()
