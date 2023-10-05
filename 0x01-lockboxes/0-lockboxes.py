#!/usr/bin/python3
"""Determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """returns True if all boxes can be opened, else False"""
# create a list to track of boxes that can be visited


visited = [False] * len(boxes)
visited = True

# a list for the keys you have
keys = [0]

while False in visited and len(keys) > 0:
    # Now get a key from the list
    key = keys.pop()
    box = boxes[key]

    for new_key in box:
        if new_key >= 0 and new_key < len(boxes) and not visited[new_key]:
            visited[new_key] = True
            keys.append(new_key)

return False not in visited
