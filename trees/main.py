

# Trees Notes
# A child node that doesn'y have any children is called a LEAF

# BINARY SEARCH TREE: numbers greater than parent node goes on the right, less than goes on the left

# BIG O - math for one node 2^1 -1 = 1, math for a tree with two leaves, so 3 nodes is
# 2^2 - 1 = 3,
# 2^3 - 1 = 7 level 3
# 2^4 - 1 = 15 level 4

# BIG O for a binary search tree is O(log n)... but the true worst case is O(n) for finding, 
# adding and removing. This is divide and conqour.

# A linked list is better for INSERT, O(1)
# Binary tree is better for LOOKUP, O(log n)
# Binary tree is better for REMOVE, O(log n)



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, value):
        new_node = Node(value)
        if self.root == None: 
            self.root = new_node
            return True

        temp = self.root

        while (True):
            if new_node.value == temp.value:
                return False

            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True  
                temp = temp.right              
            

    def contains(self,value):
        #if self.root is None:
        #    return False     This line is not necessary

        temp = self.root   

        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True 

        return False               


tree1 = BinarySearchTree()
tree1.insert(30)
tree1.insert(25)
tree1.insert(45)
tree1.insert(24)
tree1.insert(100)
tree1.insert(11)
tree1.insert(5)


# print(tree1.root.value)
# print(tree1.root.left.value)
# print(tree1.root.right.value)
print(tree1.contains(5))


