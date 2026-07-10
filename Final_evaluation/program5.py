# Q5 Binary Search Tree


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None


    def insert(self, value):
        self.root = self._insert(self.root, value)


    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        return node


    def search(self, value):
        return self._search(self.root, value)


    def _search(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search(node.left, value)

        return self._search(node.right, value)


    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)


    def preorder(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")


    def min_value(self, node):
        while node.left:
            node = node.left
        return node


    def delete(self, value):
        self.root = self._delete(self.root, value)


    def _delete(self, node, value):

        if node is None:
            return node

        if value < node.value:
            node.left = self._delete(node.left, value)

        elif value > node.value:
            node.right = self._delete(node.right, value)

        else:

            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            temp = self.min_value(node.right)

            node.value = temp.value

            node.right = self._delete(node.right, temp.value)

        return node


tree = BST()

values = [50, 30, 70, 20, 40, 60, 80, 10]

for v in values:
    tree.insert(v)

print("Inorder:")
tree.inorder(tree.root)

print("\n\nPreorder:")
tree.preorder(tree.root)

print("\n\nPostorder:")
tree.postorder(tree.root)

print("\n\nSearch 40:", tree.search(40))

print("Search 90:", tree.search(90))

tree.delete(30)

print("\nAfter deleting 30")

print("Inorder:")
tree.inorder(tree.root)

print("\n\nPreorder:")
tree.preorder(tree.root)

print("\n\nPostorder:")
tree.postorder(tree.root)

"""

Preorder:
50 30 20 10 40 70 60 80 

Postorder:
10 20 40 30 60 80 70 50 

Search 40: True
Search 90: False

After deleting 30
Inorder:
10 20 40 50 60 70 80 

Preorder:
50 40 20 10 70 60 80 

Postorder:
10 20 40 60 80 70 50 

"""