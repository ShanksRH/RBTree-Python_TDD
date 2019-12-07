class RBTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        pass
    
    def find(self, key):
        pass
    
    def delete(self, key):
        pass

class Node:
    color = 0
    left = None
    right = None
    
    def __init__(self, key=None, parent=None):
        self.key, self.parent = key, parent
