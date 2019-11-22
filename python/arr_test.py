#!/usr/bin/env python3
import png
f = open('arr_test.png', 'wb')      # binary mode is important

rows, cols = (3, 3)

arr = [[0 for i in range(cols * 3)]
       for j in range(rows)]  # [[0, 0, 0]*cols]*rows
for r in range(rows):
    for c in range(len(arr[r])):
        print(f"r:{r}, c:{c}")
        arr[r][c] = (r + 1) + (c+1)
print(arr)
w = png.Writer(cols, rows, greyscale=False)
w.write(f, arr)
f.close()

# print(arr[320][240])
