# /usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program shoots bullets and pew pew

import ugame
import stage

import constants


def menu_scene():
    # this function is the splash screen game loop

    # new pallet for filled text

    NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

    # an image bank for CircutPython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background to image 0 in the bank

    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)

    # a list of sprites that will be updated every frame
    sprites = []

    # add text objects

    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=NEW_PALETTE,
                       buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studio")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=NEW_PALETTE,
                       buffer=None)
    text2.move(40, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = text + sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        # print(keys)
        if keys & ugame.K_START != 0:
            game_scene()

        # update new game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


def game_scene():
    # this function sets the scene

    # an image bank for circuitpython
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    # a list of sprites that will be updated every frame
    sprites = []

    # buttons to keep state information
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    ship = stage.Sprite(image_bank_1, 5, int(constants.SCREEN_X / 2
                        - constants.SPRITE_SIZE / 2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE
                        + constants.SPRITE_SIZE / 2))
    sprites.append(ship)  # insert at the top of the sprite list

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)
    # create a sprite
    alien = stage.Sprite(image_bank_1, 8, 64, 56)
    sprites.append(alien)  # insert at the top of sprite list

    # create a stage for the background to show up on
    #  and set the frame rate to 60 fps
    game = stage.Stage(ugame.display, constants.FPS)
    # set the layers, items show up in order
    game.layers = sprites + [background]
    # render the background and initial location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, or you turn it off
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_X != 0:  # a button (fire)
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]
        if keys & ugame.K_X:
            pass
        if keys & ugame.K_O:
            pass
        if keys & ugame.K_START:
            pass
        if keys & ugame.K_SELECT:
            pass
        # update game logic
        # move ship to the right and the left
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)

        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)
            pass
        # move ship up and down
        if keys & ugame.K_UP:
            ship.move(ship.x, ship.y - 1)
        elif keys & ugame.K_DOWN:
            ship.move(ship.x, ship.y + 1)
            pass
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    menu_scene()
