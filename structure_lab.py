#!/usr/bin/python3
# -*-coding:Utf-8 -*


import random
import pygame

from pygame.locals import*
from constants import*

class Load_structure_map:
	def __init__(self, file):
		self.file = file
		self.structure = 0

	def load_map(self):
		list_objets = 1
		with open(self.file, "r") as file:
			structure_map = []
			for line in file:
				line_map = []
				for sprite in line:
					if sprite != '\n':
						line_map.append(sprite)
				structure_map.append(line_map)

		while list_objets < 4:
			item_x = random.randint(0, NBR_SPRITE_WIDTH - 1)
			item_y = random.randint(0, NBR_SPRITE_WIDTH - 1)
			if structure_map[item_y][item_x] == 'f':
				structure_map[item_y][item_x] = str(list_objets)
				list_objets += 1
			self.structure = structure_map

	def load_structure(self, screen):
		
		FLOOR = pygame.image.load(IMG_FLOOR).convert()
		FLOOR = pygame.transform.scale(FLOOR, (40, 40))

		WALL = pygame.image.load(IMG_WALL).convert()
		WALL = pygame.transform.scale(WALL, (40, 40))

		GUARDIAN = pygame.image.load(IMG_GARDIAN).convert()
		GUARDIAN = pygame.transform.scale(GUARDIAN, (40, 40))

		ITEM_1 = pygame.image.load(IMG_ETHER).convert()
		ITEM_1 = pygame.transform.scale(ITEM_1, (40, 40))

		ITEM_2 = pygame.image.load(IMG_NEEDLE).convert()
		ITEM_2 = pygame.transform.scale(ITEM_2, (40, 40))

		ITEM_3 = pygame.image.load(IMG_PLASTIC_TUBE).convert()
		ITEM_3 = pygame.transform.scale(ITEM_3, (40, 40))

		structure_line = 0
		for line in self.structure:
			structure_sprite = 0
			for sprite in line:
				x = structure_sprite * WIDTH_SPRITE
				y = structure_line * WIDTH_SPRITE
				if sprite == 'w':
					screen.blit(WALL, (x, y))
				if sprite == 'f':
					screen.blit(FLOOR, (x, y))
				if sprite == 'G':
					screen.blit(GUARDIAN, (x, y))
				if sprite == '1':
					screen.blit(ITEM_1, (x, y))
				if sprite == '2':
					screen.blit(ITEM_2, (x, y))
				if sprite == '3':
					screen.blit(ITEM_3, (x, y))
				structure_sprite += 1
			structure_line += 1
