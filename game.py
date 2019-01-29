#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""MacGyver Escape Game.
The principle of the game is to retrieve objects inside a labyrinth to lull
the guardian to escape this one."""

import pygame
from pygame.locals import *

from labyrinth import *
from constants import *
from macgyver import *

pygame.init()
pygame.font.init()
