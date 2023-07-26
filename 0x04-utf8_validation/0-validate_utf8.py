#!/usr/bin/python3
""" Module validates UTF-8 data encoding"""


def validUTF8(data):
    """Implement calidate UTF-8
    return True if data is a valid UTF-8 encoding
    False otherwise"""
    if type(data) is not list:
        return
    for x in data:
        if type(x) is not int:
            return
        if x > 127:
            return False
    return True
