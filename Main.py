#──────────────────────────────────────────────k
#────────██────────██────██────────────────────a
#────────██───█████──────██────────────────────k
#────────██████──────────█████████████─────────u
#────────████████████────█████████████─────────n
#────────██─────────█────██─────────██─────────a
#────────██────────██────██─────────██─────────
#────────██────────█─────██────────██──────────
#────────██───────██─────██───────███──────────
#────────██─────██───────██─────████───────────
#────────██────██────────██───████─────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#────────────────────────██────────────────────
#─────────────────────────██────────██─────────
#──────────────────────────██───────█──────────
#─────────────────────────────────██───────────
#────────────────────────────────██────────────
#────────████████████─────────███──────────────
#───────────────────────────██─────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
#──────────────────────────────────────────────
# AVL AND BINARY TREE


import random

class Node:
    #Creating node with his keys an left and right values
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.height = 1

class BinaryTree:
    def __init__(self, root=None):  # Defining root as None
        self.root = root

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left:
                self._insert_recursive(current_node.left, key)
            else:
                current_node.left = Node(key)
        elif key > current_node.key:
            if current_node.right:
                self._insert_recursive(current_node.right, key)
            else:
                current_node.right = Node(key)
        else:
            # If key already exists do nothing 
            pass

    def is_balanced(self):
        return self._is_balanced_recursive(self.root) != -1

    def _is_balanced_recursive(self, node):
        if not node:
            return 0

        left_height = self._is_balanced_recursive(node.left)
        if left_height == -1:
            return -1

        right_height = self._is_balanced_recursive(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
    
class AVLTree(BinaryTree):
    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # Inserting like is a 'normal' Binary Tree
        if not node:
            return Node(key)
        elif key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)

        # Updating node height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Node Balance Factor
        balance_factor = self._get_balance(node)

        # Rotation Case
        if balance_factor > 1 and key < node.left.key:
            return self._rotate_right(node)
        if balance_factor < -1 and key > node.right.key:
            return self._rotate_left(node)
        if balance_factor > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance_factor < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y
    
# Tree Traversal Techniques

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.key, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.key, end=" ")
        



# TESTING
if __name__ == "__main__":
    BiTree = BinaryTree()
    AvTree = AVLTree()
 
    for i in range(13):
       key = random.randint(1, 1000)
       BiTree.insert(key)
       AvTree.insert(key)

    while True:
        print("\nMenu:")
        print("1 - Inorder Traversal")
        print("2 - Preorder Traversal")
        print("3 - Postorder Traversal")
        print("4 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nInorder Traversal of Binary Tree:")
            inorder_traversal(BiTree.root)
            print("\nInorder Traversal of AVL Tree:")
            inorder_traversal(AvTree.root)
        elif choice == '2':
            print("\nPreorder Traversal of Binary Tree:")
            preorder_traversal(BiTree.root)
            print("\nPreorder Traversal of AVL Tree:")
            preorder_traversal(AvTree.root)
        elif choice == '3':
            print("\nPostorder Traversal of Binary Tree:")
            postorder_traversal(BiTree.root)
            print("\nPostorder Traversal of AVL Tree:")
            postorder_traversal(AvTree.root)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")