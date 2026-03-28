

# Trees Notes
# A child node that doesn'y have any children is called a LEAF

# BINARY SEARCH TREE: numbers greater than parent node goes on the right, less than goes on the left


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


