#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
!!!! MacGyver Escape Game !!!!
Author: Jimi Bourgeois
Version: 20190225
Project: Project 3 OpenClassrooms
Code language: Python3
Coding: Utf-8
"""
#import the game interface module
import pygame
#import modules for game operation
from pygame.locals import *
from structure_lab import *
from constants import *
from macgyver import *

def main():
	"""
		Initializes the game's interface, window size, name the window
		and game menu

		Main loop of the game:
		Displays the maze in its various states after the player moves
		The player recovers the objects simply by moving on them
		The objects are placed randomly each time the game is loaded
		A counter indicates the progress of recovery of objects
		The player wins under the condition to retrieve all the objects and
		find the goalkeeper to go out otherwise the player loses
	"""

	pygame.init()
	#initialize the size of the window
	screen = pygame.display.set_mode((SIZE_SCREEN_WIDTH, SIZE_SCREEN_HEIGTH))
	#window name
	pygame.display.set_caption('MacGyver Escape Game')

	#main loop
	main_loop = 1
	while main_loop:
		#Formatting the game menu
		background = pygame.image.load(IMG_BACK).convert()
		bfont = pygame.image.load(IMG_BFONT).convert()
		screen.blit(bfont, (0, 600))
		screen.blit(background, (0, 0))
		pygame.display.update()

		#Loop of game menu and choice of level
		#Preventive loop in case of setting up several levels
		game_loop = 1
		home_loop = 1
		while home_loop:
			#limit of frame
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					home_loop = 0
					game_loop = 0
					main_loop = 0
					choice = 0
				elif event.type == KEYDOWN:
					if event.key == K_RETURN:
						home_loop = 0
						choice = 'map.txt'

		#Loading the chosen level
		if choice != 0:
			level = Load_structure_map(choice)
			level.load_map()
			level.load_structure(screen)

			mg = Character(IMG_MAC, level)

		#Loop of the game, update of the screen of the movement of the player
		#according to the direction taken, according to the collection of
		#objects and conditions of exit
		while game_loop:
			#limit of frame
			pygame.time.Clock().tick(30)
			for event in pygame.event.get():
				if event.type == QUIT:
					game_loop = 0
					home_loop = 0

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						game_loop = 0
					elif event.key == K_RIGHT:
						mg.move('right')
					elif event.key == K_LEFT:
						mg.move('left')
					elif event.key == K_UP:
						mg.move('up')
					elif event.key == K_DOWN:
						mg.move('down')

					level.load_structure(screen)
					screen.blit(mg.direction, (mg.x, mg.y))
					pygame.display.flip()

					#Display of objects recovery
					no_items = pygame.image.load(IMG_NO_ITEMS).convert()
					screen.blit(no_items, (180, 600))
					pygame.display.flip()

				if len(mg.item_loot) == 1:
					items_1_3 = pygame.image.load(IMG_ITEMS_1_3).convert()
					screen.blit(items_1_3, (180, 600))
					pygame.display.flip()

				if len(mg.item_loot) == 2:
					items_2_3 = pygame.image.load(IMG_ITEMS_2_3).convert()
					screen.blit(items_2_3, (180, 600))
					pygame.display.flip()

				if len(mg.item_loot) == 3:
					items_3_3 = pygame.image.load(IMG_ITEMS_3_3).convert()
					screen.blit(items_3_3, (180, 600))
					pygame.display.flip()

				#Exit conditions
				if level.structure[mg.mg_y][mg.mg_x] == 'G':
					if len(mg.item_loot) == 3:
						#Victory screen display
						win = pygame.image.load(IMG_MACWIN).convert()
						bfont = pygame.image.load(IMG_BFONT).convert()
						screen.blit(bfont, (0, 600))
						screen.blit(win, (0, 0))
						pygame.display.update()
						home_loop = 0

					else:
						#Defeat screen display
						loose = pygame.image.load(IMG_MACLOOSE).convert()
						bfont = pygame.image.load(IMG_BFONT).convert()
						screen.blit(bfont, (0, 600))
						screen.blit(loose, (0, 0))
						pygame.display.update()
						home_loop = 0


if __name__ == "__main__":
	main()
