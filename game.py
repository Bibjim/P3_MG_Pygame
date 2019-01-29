#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""MacGyver Escape Game.
The principle of the game is to retrieve objects inside a labyrinth to lull
the guardian to escape this one."""

import pygame
from pygame.locals import *

from labyrinth import Labyrinth
from constants import Constants
from macgyver import Perso

pygame.init()
pygame.font.init()

def main():
	screen = pygame.display.set_mode((Constants.SIZE_WINDOW, Constants.SIZE_WINDOW))
	pygame.display.set_caption(Constants.TITLE_WINDOW)

	icone = pygame.image.load(Constants.MACGYVER_IMAGE)
	pygame.display.set_icon(icone)

	background = pygame.image.load(Constants.BACKGROUND_IMAGE).convert()

	labyrinth = Labyrinth()
	labyrinth.generate_map()
	labyrinth.display_labyrinth()

	macgyver = Perso("ressource/MacGyver.png", labyrinth)

	cont = 1
	while cont:

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				cont = 0
				if event.type == KEYDOWN:
					if event.key == K_RIGHT:
						macgyver.move('right')
					elif event.key == K_LEFT:
						macgyver.move('left')
					elif event.key == K_UP:
						macgyver.move('up')
					elif event.key == K_DOWN:
						macgyver.move('down')

		screen.blit(background, (0, 0))
		labyrinth.display_labyrinth()

		if labyrinth.sturture[macgyver.mg_cell_y][macgyver.mg_cell_x] == 'G':
			cont = 0

if __name__ == "__main__":
    main()
