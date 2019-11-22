#!/usr/bin/env python3

import sys
import png
import random

# https://en.wikipedia.org/wiki/Barnsley_fern

image_width = 1280
image_height = 720


def setup():
    rows, cols = (image_height, image_width)
    image_arr = [[0 for c in range(cols * 3)]
                 for r in range(rows)]
    #[[0, 0, 0]*cols]*rows
    return image_arr


def draw_point(image_arr, point, scale_x=85, scale_y=57,  offset_x=640, offset_y=50):
    # 57 is to scale the fern and -275 is to start the drawing from the bottom.
    x = point[0]
    y = point[1]
    randGreen = random.randint(128, 255)

    clamped_x = (int(3 * scale_x * x) + int(image_width))
    clamped_y = (int(scale_y * y) + offset_y)

    # print(f"point = x:{clamped_x}, y:{clamped_y}")
    if (clamped_x + 1) % 3 == 0:
        clamped_x = clamped_x + 1
        # print(f"move -> = x:{clamped_x}, y:{clamped_y}")
    elif (clamped_x + 1) % 3 == 2:
        clamped_x = clamped_x - 1
        # print(f"move <- = x:{clamped_x}, y:{clamped_y}")

    image_arr[clamped_y][clamped_x + 1] = randGreen

    return image_arr


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


def draw(image_arr):
    point = (0, 0)
    for n in range(100_000):
        point = next_point(point)
        # print(f"next point {point}")
        image_arr = draw_point(image_arr, point)

    # print(image_arr)
    rows, cols = (image_height, image_width)
    f = open('fern_arr.png', 'wb')
    w = png.Writer(cols, rows, greyscale=False)
    w.write(f, image_arr)
    f.close()


def main():
    image_arr = setup()
    draw(image_arr)


main()
