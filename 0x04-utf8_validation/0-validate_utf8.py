#!/usr/bin/python3
""" Module validates UTF-8 data encoding"""


def validUTF8(data):
    """Implement calidate UTF-8
    return True if data is a valid UTF-8 encoding
    False otherwise"""
    count = 0
    for x in data:
        if count == 0:
            if x >> 5 == 0b110:
                count = 1
            elif x >> 4 == 0b1110:
                count = 2
            elif x >> 0b011110:
                count = 3
            elif x >> 7 == 1:
                return False
        else:
            if x >> 6 != 0b10:
                return False
    return True
