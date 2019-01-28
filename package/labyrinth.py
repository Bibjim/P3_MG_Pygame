#!/usr/bin/python3
# -*- coding: Utf-8 -*


"""Definition of class for the labyrinth"""

import pygame
from pygame.locals import *
from package.constantes import *

class Level:
	def __init__(self, file):
		self.file = file
		self.structure = 0


	def open_map(self):
		with open(self.file, "r") as file:
			structure_level = []
			for line in file:
				line_level = []
				for sprite in line:
					if sprite != '\n':
						line_level.append(sprite)
				structure_level.append(line_level)
			self.structure = structure_level


	def display_lab(self, window):
		wall = pygame.image.load(WALL_IMAGE).convert()
		floor = pygame.image.load(FLOOR_IMAGE).convert()
		guardian = pygame.image.load(GUARDIAN_IMAGE).convert_alpha()

		num_line = 0
		for line in self.structure:
			num_case = 0
			for sprite in line:
				x = num_case * CELL_SIZE
				y = num_line * CELL_SIZE
				if sprite == 'w':
					window.blit(wall, (x,y))
				elif sprite == 'F':
					window.blit(floor, (x,y))
				elif sprite == 'g':
					window.blit(guardian, (x,y))
				num_case += 1
			num_line += 1




class MacGyver:
	def __init__(self, level):
		macgyver = pygame.image.load(MACGYVER_IMAGE).convert()
		self.case_x = 0
		self.case_y = 14
		self.x = 0
		self.y = 14
		self.level = level


	def movement(self, move):
		if move == 'right':
			if self.case_x < (NBR_SPRITE - 1):
				if self.level.structure[self.case_y][self.case_x+1] != 'w':
					self.case_x += 1
					self.x = self.case_x * CELL_SIZE
		if move == 'left':
			if self.case_x > 0:
				if self.level.structure[self.case_y][self.case_x-1] != 'w':
					self.case_x -= 1
					self.x = self.case_x * CELL_SIZE
		if move == 'up':
			if self.case_y > 0:
				if self.level.structure[self.case_y-1][self.case_x] != 'w':
					self.case_y -= 1
					self.y = self.case_y * CELL_SIZE
		if move == 'down':
			if self.case_y < (NBR_SPRITE - 1):
				if self.level.structure[self.case_y+1][self.case_x] != 'w':
					self.case_y += 1
					self.y = self.case_y * CELL_SIZE
