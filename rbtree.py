class RBTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        pass
    
    def find(self, key):
        if self.root == None:
            return False
        return self.root.find(key)
    
    def delete(self, key):
        pass

class Node:
    color = 0
    left = None
    right = None
    
    def __init__(self, key=None, parent=None):
        self.key, self.parent = key, parent

    def find(self, key):
        if self.key == key:
            return True
        if self.key > key:
            if self.left == None:
                return False
            return self.left.find(key)
        if self.right == None:
            return False
        return self.right.find(key)
