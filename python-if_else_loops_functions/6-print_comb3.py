#!/usr/bin/python3
for i in range(89):
    if i // 10 < i % 10:
        print("{:02d}".format(i), end=', ')
print("{:02d}".format(89))
