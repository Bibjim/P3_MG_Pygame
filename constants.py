#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Definition of game constants:
    - formatting the game window
    - formatting the size of the game map
    - list of images of the characters in the game
    - list of images of game objects
    - list of game structure images
"""
class Constants:
    #formatting the game window
    TITLE_WINDOW = "MacGyver Escape Game"
    ICON_WINDOW = "ressource/MacGyver.png"
    BACKGROUND_IMAGE = "ressource/Background_img.jpg"

    #formatting the size of the game map
    NBR_SPRITE = 15
    SIZE_SPRITE = 40
    SIZE_WINDOW = NBR_SPRITE * SIZE_SPRITE

    #list of images of the characters in the game
    MACGYVER_IMAGE = "ressource/MacGyver.png"
    GUARDIAN_IMAGE = "ressource/Gardien.png"
    OPTIONAL_PERSO_IMAGE = "ressource/personnages.png"

    #list of images of game objects
    NEEDLE_IMAGE = "ressource/aiguille.png"
    ETHER_IMAGE = "ressource/ether.png"
    SYRINGE_IMAGE = "ressource/seringe.png"
    PLASTIC_TUBE_IMAGE = "ressource/tube_plastique.png"

    #list of game structure images
    WALL_IMAGE = "ressource/Wall.png"
    FLOOR_IMAGE = "ressource/Floor.png"
