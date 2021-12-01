# My First PyGame, Ashley Wright, 12/1/21, 1:40pm, v0.4

import pygame, sys 
from pygame.locals import * 

# Start PyGame
pygame.init()

# Setup our window. 
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello, world!')

# Setup Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WONKYPURPLE = (147, 138, 180)

# Setup font.
basicfont = pygame.font.SysFont(None, 48)

# Setup text.
text = basicFont.render('Hello, world', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Fill background color.
windowSurface.fill(WONKYPURPLE)

# Draw a polygon onto the screen.
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106),(236, 277), (56, 277), (0, 106)))
