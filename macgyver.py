#!/usr/bin/python3
# -*-coding:Utf-8 -*

import pygame

from pygame.locals import*
from constants import*
from structure_lab import*



class Character:
	"""
	Player creation class, initialization of his position on the map
	Management of the player's move so that he can move this box
	in the structure of the labyrinth
	Conditions of movement limited by walls
	"""

	def __init__(self, MacGyver, level):
		#Initialization of the player in the map
		#Opening the player's image
		#Scale image to the size of a sprite
		self.MacGyver = pygame.image.load(IMG_MAC).convert_alpha()
		self.MacGyver = pygame.transform.scale(self.MacGyver, (40, 40))
		self.mg_x = 0
		self.mg_y = 0
		self.x = 0
		self.y = 0

		self.direction = self.MacGyver
		self.level = level
		self.item_loot = []

	def move(self, direction):
		#Determine the player's position according to the desired direction
		mg_pos = 0
		if direction == 'right':
			if self.mg_x < (NBR_SPRITE_WIDTH - 1):
				if self.level.structure[self.mg_y][self.mg_x+1] != 'w':
					self.mg_x += 1
					self.x = self.mg_x * WIDTH_SPRITE
					item = self.level.structure[self.mg_y][self.mg_x]
					if item != 'f' and item != 'G':
						mg_pos = item
						self.level.structure[self.mg_y][self.mg_x] = 'f'

		elif direction == 'left':
			if self.mg_x > 0:
				if self.level.structure[self.mg_y][self.mg_x-1] != 'w':
					self.mg_x -= 1
					self.x = self.mg_x * WIDTH_SPRITE
					item = self.level.structure[self.mg_y][self.mg_x]
					if item != 'f' and item != 'G':
						mg_pos = item
						self.level.structure[self.mg_y][self.mg_x] = 'f'

		elif direction == 'up':
			if self.mg_y > 0:
				if self.level.structure[self.mg_y-1][self.mg_x] != 'w':
					self.mg_y -= 1
					self.y = self.mg_y * WIDTH_SPRITE
					item = self.level.structure[self.mg_y][self.mg_x]
					if item != 'f' and item != 'G':
						mg_pos = item
						self.level.structure[self.mg_y][self.mg_x] = 'f'

		elif direction == 'down':
			if self.mg_y < (NBR_SPRITE_WIDTH - 1):
				if self.level.structure[self.mg_y+1][self.mg_x] != 'w':
					self.mg_y += 1
					self.y = self.mg_y * WIDTH_SPRITE
					item = self.level.structure[self.mg_y][self.mg_x]
					if item != 'f' and item != 'G':
						mg_pos = item
						self.level.structure[self.mg_y][self.mg_x] = 'f'
		#The items collected are added to the list
		if mg_pos != 0 and mg_pos != 'G':
			self.item_loot.append(mg_pos)
