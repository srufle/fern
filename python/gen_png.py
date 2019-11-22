#!/usr/bin/env python3

import png
f = open('ramp.png', 'wb')      # binary mode is important
w = png.Writer(256, 1, greyscale=True)
w.write(f, [range(256)])
f.close()

s = ['110010010011',
     '101011010100',
     '110010110101',
     '100010010011']
s = [[int(c) for c in row] for row in s]

w = png.Writer(len(s[0]), len(s), greyscale=True, bitdepth=1)
f = open('png.png', 'wb')
w.write(f, s)
f.close()

s = ['110010010011',
     '101011010100',
     '110010110101',
     '100010010011']
s = [[int(c) for c in row] for row in s]

palette = [(0x55, 0x55, 0x55), (0xff, 0x99, 0x99)]
w = png.Writer(len(s[0]), len(s), palette=palette, bitdepth=1)
f = open('png2.png', 'wb')
w.write(f, s)

p = [(255, 0, 0, 0, 255, 0, 0, 0, 255),
     (128, 0, 0, 0, 128, 0, 0, 0, 128)]
f = open('swatch.png', 'wb')
w = png.Writer(3, 2, greyscale=False)
w.write(f, p)
f.close()
