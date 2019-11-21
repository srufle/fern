#!/usr/bin/env python3

import turtle
import random
import time
import signal
import sys

# https://en.wikipedia.org/wiki/Barnsley_fern


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


def setup():
    pen = turtle.Turtle()
    pen.speed(.002)
    pen.color('green')
    pen.penup()

    return pen


def draw_point(pen, point, scale_x=85, scale_y=57,  offset_y=275):
    # 57 is to scale the fern and -275 is to start the drawing from the bottom.
    x = point[0]
    y = point[1]
    # print(f"draw point {x}, {y}")
    pen.goto(scale_x * x, (scale_y * y) - offset_y)
    pen.pendown()
    pen.dot()
    pen.penup()


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


def draw(pen):
    point = (0, 0)
    draw_point(pen, point)
    for n in range(10):
        point = next_point(point)
        draw_point(pen, point)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    pen = setup()
    draw(pen)
    print('Press Ctrl+C')
    signal.pause()


main()
