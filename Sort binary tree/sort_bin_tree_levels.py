'''
Sort by level traversal
'''
from collections import deque
class Node:
    '''
    Node for tree
    '''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    '''
    Sorting function
    '''
    if not node:
        return []
    q = deque([node])
    result = []

    while q:
        curr = q.popleft()
        result.append(curr.value)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return result
