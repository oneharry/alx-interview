#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Function checks if all box in boxes list can be opened by a key
        returns true else return false
    """
    new_list = boxes
    for i in range(1, len(boxes)):
        for idx in range(len(new_list)):
            if idx == i:
                continue
            if i in new_list[idx] or new_list[idx] is []:
                status = 0
                break
            else:
                status = 1
                continue
        if status == 1:
            return False
    return True
