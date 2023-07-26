#!/usr/bin/python3
""" Module validates UTF-8 data encoding"""


def validUTF8(data):
    """Implement calidate UTF-8
    return True if data is a valid UTF-8 encoding
    False otherwise"""
    for x in data:
        if x.bit_length() > 7:
            return False
    return True
