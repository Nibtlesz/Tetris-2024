"""
Juego de Tetris
Versión: 1.0
Autor: Nibtlesz
Language: Python 3.12
"""
import pygame
import random

pygame.font.init()

# GLOBALS VARS
S_WIDTH = 800
S_HEIGHT = 700
PLAY_WIDTH = 300  # MEANING 300 // 10 = 30 WIDTH PER BLOCK
PLAY_HEIGHT = 600  # MEANING 600 // 20 = 30 HEIGHT PER BLOCK
BLOCK_SIZE = 30

TOP_LEFT_X = (S_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = S_HEIGHT - PLAY_HEIGHT

#  SHAPE FORMATS

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]
