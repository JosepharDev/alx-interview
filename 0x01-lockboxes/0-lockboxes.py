#!/usr/bin/emv python3
""" This is a graph traversal problem where each box is a node
    and the keys in the box represent edges to other nodes (boxes)"""


def canUnlockAll(boxes):
    """  The task is to check if you can reach all nodes (open all boxes)
        starting from node 0 (the first box)"""
    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)
    return len(unlocked) == n
