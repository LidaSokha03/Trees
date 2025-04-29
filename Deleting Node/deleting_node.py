def deleteNode(self, root, key: int):
    if not root:
        return None
    else:
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            min_node = self.min_node(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
    return root
