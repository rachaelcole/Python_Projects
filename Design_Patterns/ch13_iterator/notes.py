# Iterator pattern
# Consider a binary tree data structure as follows:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Traversing the elements of the tree might look something like this:
def tree_traverse(node):
    print(node.data)
    if node.left is not None:
        tree_traverse(node.left)
    if node.right is not None:
        tree_traverse(node.right)
    print(node.data)

if __name__ == "__main__":
    root = Node('I am the root')
    root.left = Node('first left child')
    root.right = Node('first right child')
    root.left.right = Node('Right child of first left child of root')
    tree_traverse(root)


# Reference: 
# Badenhurst, Wessel. "Chapter 13: Iterator Pattern". Practical Python Design Patterns: Pythonic Solutions to Common Problems, Apress, October 20, 2017, pp. 203-217,
# DOI: https://doi.org/10.1007/978-1-4842-2680-3_13.