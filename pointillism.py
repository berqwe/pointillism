#Bereket Ashebir Alemu 101282366

import pygame
import random
import sys

# loads the source image
src_img = pygame.image.load(sys.argv[1])

# gets the height and width of source image
(wid, hgt) = src_img.get_size()
# scales up the screen
win_sfc = pygame.display.set_mode((wid*5, hgt*5))

# nested loop to visit each pixel
for y in range(hgt):
    for x in range(wid):
        # get the colour value of each pixel
        (r, g, b, _) = src_img.get_at((x, y))
        # gets the number of required circles
        red = r//50
        green = g//50
        blue = b//50
        xLoc= x*5
        yLoc= y*5
        # draws the required number of circle
        for i in range(red):
            pix_x = random.randint(xLoc,xLoc+5)
            pix_y = random.randint(yLoc,yLoc+5)
            pygame.draw.circle(win_sfc,(255,0,0),(pix_x,pix_y),1)
        for i in range(green):
            pix_x = random.randint(xLoc,xLoc+5)
            pix_y = random.randint(yLoc,yLoc+5)
            pygame.draw.circle(win_sfc,(0,255,0),(pix_x,pix_y),1)
        for i in range(blue):
            pix_x = random.randint(xLoc,xLoc+5)
            pix_y = random.randint(yLoc,yLoc+5)
            pygame.draw.circle(win_sfc,(0,0,255),(pix_x,pix_y),1)

# updates the screen
pygame.display.update()

# keeps the window opened until user close it
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

