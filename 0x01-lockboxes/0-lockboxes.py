#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """returns True if all boxes can be opened, else False"""
    # create a list to track of boxes that can be visited

    visited = [False] * len(boxes)
    visited[0] = True

    # a list for the keys you have
    keys = [0]

    while not all(visited) and keys:
        # Now get a key from the list
        key = keys.pop()
        box = boxes[key]

        for new_key in box:
            if 0 <= new_key < len(boxes) and not visited[new_key]:
                visited[new_key] = True
                keys.append(new_key)

    return all(visited)
