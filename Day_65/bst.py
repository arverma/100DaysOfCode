class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self, root, data):
        if root == None:
            root = node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root
    
    def search(self, root, k):
        if root == None:
            return False
        if k == root.data:
            return True
        elif k < root.data:
            return self.search(root.left, k)
        else:
            return self.search(root.right, k)
    
    def height(self, root):
        if root == None:
            return -1
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return max(r_height, l_height) + 1
    
    def check_if_BST(self, root):
        global arr
        arr = []
        arr = self.check_if_BST_util(root)
        print(arr)
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    
    def check_if_BST_util(self, root):
        if root != None:
            self.check_if_BST_util(root.left)
            arr.append(root.data)
            self.check_if_BST_util(root.right)
        return arr
            
    def traverse_inorder(self, root):
        if root != None:
            self.traverse_inorder(root.left)
            print(root.data, end=" ")
            self.traverse_inorder(root.right)
            
    def traverse_preorder(self, root):
        if root != None:
            print(root.data, end=" ")
            self.traverse_preorder(root.left)
            self.traverse_preorder(root.right)
    
    def traverse_postorder(self, root):
        if root != None:
            self.traverse_postorder(root.left)
            self.traverse_postorder(root.right)
            print(root.data, end=" ")
        

tree = BST()
root = tree.insert(None, 10)
root = tree.insert(root, 15)
root = tree.insert(root, 2)
root = tree.insert(root, 25)
root = tree.insert(root, 45)
root = tree.insert(root, 5)
root = tree.insert(root, 4)
root = tree.insert(root, 21)
tree.traverse_inorder(root)
print()
tree.traverse_preorder(root)
print()
tree.traverse_postorder(root)
print()
print(tree.search(root, 6))
print(tree.search(root, 25))
print(tree.search(root, 4))
print(tree.height(root))
print()
print(tree.check_if_BST(root))
