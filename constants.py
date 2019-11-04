#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program makes sure that the sprite doesn’t go off the screen


SCREEN_X = 160
SCREEN_Y = 120
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FPS = 60

# Using for button space
button_state = {
    "button_up": "up,",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
