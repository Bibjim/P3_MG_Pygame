#!/usr/bin/python3
# -*- coding: Utf-8 -*


"""Definition of class for the labyrinth"""

import pygame
from pygame.locals import *

from constants import Constants

class Labyrinth:
	def __init__(self, file):
		self.file = file
		self.structure = 0

	def generate_map(self):
		with open(self.file, "r") as file:
			structure_map = []
			for line in file
			line_map = []
			for sprite in line:
				if sprite != '\n':
					line_map.append(sprite)

    def display_labyrinth(self, img):
        WALL_IMAGE = pygame.image.load("ressource/Wall.png").convert()
        FLOOR_IMAGE = pygame.image.load("ressource/Floor.png").convert()
        GUARDIAN_IMAGE = pygame.image.load("ressource/Gardien.png").convert_alpha()
        line_number = 0
        for line in self.structure:
            column_number = 0
            for sprite in line:
                x = column_number * Constants.SIZE_SPRITE
                y = line_number * Constants.SIZE_SPRITE
                if sprite == 'w':
                    img.blit(WALL_IMAGE, (x, y))
                elif sprite == 'F':
                    img.blit(FLOOR_IMAGE, (x, y))
                elif sprite == 'G':
                    img.blit(GUARDIAN_IMAGE, (x, y))
                column_number += 1
            line_number += 1
