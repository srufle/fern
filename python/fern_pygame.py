#!/usr/bin/env python3

import sys
import pygame
import random

# https://en.wikipedia.org/wiki/Barnsley_fern


def setup():
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    black = 0, 0, 0
    screen.fill(black)
    return screen


def draw_point(fern_area, point, scale_x=85, scale_y=57,  offset_y=275):
    # 57 is to scale the fern and -275 is to start the drawing from the bottom.
    x = point[0]
    y = point[1]
    fern_color = pygame.Color(0, 255, 0)
    clamped_point = (int(scale_x * x) + 320, int((scale_y * y)))
    fern_area.set_at(clamped_point, fern_color)
    return fern_area


def next_point(point):
    # print("next point")
    r = random.random()  # to get probability
    r = r*100
    last_x = point[0]
    last_y = point[1]
    # elif ladder based on the probability
    if r < 1:
        x = 0
        y = 0.16*last_y
    elif r < 86:
        x = 0.85*last_x + 0.04*last_y
        y = -0.04*last_x + 0.85*last_y + 1.6
    elif r < 93:
        x = 0.20*last_x - 0.26*last_y
        y = 0.23*last_x + 0.22*last_y + 1.6
    else:
        x = -0.15*last_x + 0.28*last_y
        y = 0.26*last_x + 0.24*last_y + 0.44
    return (x, y)


def draw(screen):
    fern_area = pygame.Surface((1280, 720))
    black = 0, 0, 0
    point = (0, 0)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        point = next_point(point)
        # print(f"next point {point}")
        fern_area = draw_point(fern_area, point)
        screen.blit(fern_area, (0, 0))
        pygame.display.flip()


def main():
    screen = setup()
    draw(screen)


main()
