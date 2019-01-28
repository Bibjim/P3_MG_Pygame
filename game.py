#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""MacGyver Escape Game.
The principle of the game is to retrieve objects inside a labyrinth to lull
the guardian to escape this one."""

import pygame
from pygame.locals import *

from package.labyrinth import *
from package.constantes import *

WINDOW_GAME = pygame.display.set_mode((SIZE_WINDOW, SIZE_WINDOW))

pygame.display.set_icon(ICON_WINDOW)

pygame.display.set_caption(TITLE_WINDOW)

pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    continuer = int(input())
