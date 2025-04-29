'''
Binary tree traversal
'''
class Node:
    '''
    Node for the tree
    '''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    '''
    Preorder traversal
    '''
    if not node:
        return []
    else:
        return [node.data] + pre_order(node.left) + pre_order(node.right)

def in_order(node):
    '''
    Inorder traversal
    '''
    if not node:
        return []
    else:
        return in_order(node.left) + [node.data] + in_order(node.right)

def post_order(node):
    '''
    Postorder traversal
    '''
    if not node:
        return []
    else:
        return post_order(node.left) + post_order(node.right) + [node.data]
