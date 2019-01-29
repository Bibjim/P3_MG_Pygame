#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame

from pygame.locals import *
from constants import Constants


class Perso:
    def __init__(self, MACGYVER_IMAGE, lab):
        self.image = pygame.image.load(MACGYVER_IMAGE).convert_alpha()
        self.mg_cell_x = 0
        self.mg_cell_y = 14
        self.mg_x = self.mg_cell_x * Constants.SIZE_SPRITE
        self.mg_y = self.mg_cell_y * Constants.SIZE_SPRITE
        self.lab = lab

    def move(self, direction):

        def move_right():
            self.mg_cell_x += 1
            self.mg_x = self.mg_cell_x * Constants.SIZE_SPRITE

        def move_left():
            self.mg_cell_x -= 1
            self.mg_x = self.mg_cell_x * Constants.SIZE_SPRITE

        def move_up():
            self.mg_cell_y -= 1
            self.mg_y = self.mg_cell_y * Constants.SIZE_SPRITE

        def move_down():
            self.mg_cell_y += 1
            self.mg_y = self.mg_cell_y * Constants.SIZE_SPRITE

        if direction == 'right':
            if self.mg_cell_x < (Constants.NBR_SPRITE - 1):
                if self.lab.structure[self.mg_cell_y][self.mg_cell_x + 1] != 'w':
                    move_right()
        if direction == 'left':
            if self.mg_cell_x > 0:
                if self.lab.structure[self.mg_cell_y][self.mg_cell_x - 1] != 'w':
                    move_left()
        if direction == 'up':
            if self.mg_cell_y > 0:
                if self.lab.structure[self.mg_cell_y - 1][self.mg_cell_x] != 'w':
                    move_up()
        if direction == 'down':
            if self.mg_cell_y < (Constants.NBR_SPRITE - 1):
                if self.lab.structure[self.mg_cell_y + 1][self.mg_cell_x] != 'w':
                    move_down()
