#!/usr/bin/python3
# -*-coding:Utf-8 -*

#module import to create an algorithm
import random
#import the game interface module
import pygame
#import modules for game operation
from pygame.locals import*
from constants import*

class Load_structure_map:
    """
	Class that creates the labyrinth structure, opening the file
	.txt source, creating a list of list to generate a 2D map according to
	2 axes. In this map, the use of the Random module is necessary for
	generate 3 objects randomly in the labyrinth corridors
	Loading images according to the structure of the map and the location
    of objects
	"""
    def __init__(self, file):
        """
        initialization of the source file and the structure of the labyrinth
        """
        self.file = file
        self.structure = 0

    def load_map(self):
        """
        Opening map elements in a list
        """
        list_objets = 1
        with open(self.file, "r") as file:
            structure_map = []
            for line in file:
                line_map = []
                for sprite in line:
                    if sprite != '\n':
                        line_map.append(sprite)
                structure_map.append(line_map)

		#Random placement of objects in labyrinth structure
        while list_objets < 4:
            item_x = random.randint(0, NBR_SPRITE_WIDTH - 1)
            item_y = random.randint(0, NBR_SPRITE_WIDTH - 1)
            if structure_map[item_y][item_x] == 'f':
                structure_map[item_y][item_x] = str(list_objets)
                list_objets += 1
            self.structure = structure_map

    def load_structure(self, screen):
        """
        Opening images corresponding to the structure of the labyrinth
		Scale images to the size of a sprite
        """
        DEPARTURE = pygame.image.load(IMG_DEPARTURE).convert()
        DEPARTURE = pygame.transform.scale(DEPARTURE, (40, 40))

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

        #Formatting the labyrinth structure with the images
        structure_line = 0
        for line in self.structure:
            structure_sprite = 0
            for sprite in line:
                mg_pos_x = structure_sprite * WIDTH_SPRITE
                mg_pos_y = structure_line * WIDTH_SPRITE
                if sprite == 'D':
                    mg_pos_dep = screen.blit(DEPARTURE, (mg_pos_x, mg_pos_y))
                    self.mg_pos_dep = [mg_pos_x, mg_pos_y]
                if sprite == 'w':
                    screen.blit(WALL, (mg_pos_x, mg_pos_y))
                if sprite == 'f':
                    screen.blit(FLOOR, (mg_pos_x, mg_pos_y))
                if sprite == 'G':
                    screen.blit(GUARDIAN, (mg_pos_x, mg_pos_y))
                if sprite == '1':
                    screen.blit(ITEM_1, (mg_pos_x, mg_pos_y))
                if sprite == '2':
                    screen.blit(ITEM_2, (mg_pos_x, mg_pos_y))
                if sprite == '3':
                    screen.blit(ITEM_3, (mg_pos_x, mg_pos_y))
                structure_sprite += 1
            structure_line += 1

    def MacGyver_init_pos(self):
        """
        Methode to initialize position Player
        """
        return self.mg_pos_dep
