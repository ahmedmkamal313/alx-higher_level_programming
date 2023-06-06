#!/usr/bin/python3
for i in range(122, 65, -1):
    print("{:c}".format(i if i % 2 else i - 32), end="")
