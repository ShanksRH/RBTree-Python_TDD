class RBTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
            return True
        res = self.root.insert(key)
        while self.root.parent != None:
            self.root = self.root.parent
        return res
    
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

    def copy(self, node):
        self.left, self.right, self.parent, self.left, self.color = \
        node.left, node.right, node.parent, node.left, node.color

    def grandparent(self):
        if self.parent == None:
            return None
        return self.parent.parent
    
    def uncle(self):
        g = self.grandparent()
        if g == None:
            return None
        if self.parent == g.left:
            return g.right
        return g.left
    
    def reconnect(self, other):
        other.parent = self.parent
        if self.parent != None:
            if self.parent.left == self:
                self.parent.left = other
            else:
                self.parent.right = other
        self.parent = other

    def rotate_right(self):
        pivot = self.left
        self.reconnect(pivot)
        self.left = pivot.right
        if pivot.right != None:
            pivot.right.parent = self
        pivot.right = self

    def rotate_left(self):
        pivot = self.right
        self.reconnect(pivot)
        self.right = pivot.left
        if pivot.left != None:
            pivot.left.parent = self
        pivot.left = self
    
    def insert_case1(self):
        if self.parent == None:
            self.color = 0
        else:
            self.insert_case2()
    
    def insert_case2(self):
        if self.parent.color != 0:
            self.insert_case3()
    
    def insert_case3(self):
        u = self.uncle()
        if u != None and u.color == 1:
            self.parent.color, u.color = 0, 0
            g = self.grandparent()
            g.color = 1
            g.insert_case1()
        else:
            self.insert_case4()

    def insert_case4(self):
        g = self.grandparent()
        if self == self.parent.right and self.parent == g.left:
            self.parent.rotate_left()
            self.copy(self.left)
        elif self == self.parent.left and self.parent == g.right:
            self.parent.rotate_right()
            self.copy(self.right)
        self.insert_case5(g)

    def insert_case5(self, g):
        self.parent.color, g.color = 0, 1
        if self == self.parent.left and self.parent == g.left:
            g.rotate_right()
        else:
            g.rotate_left()
    
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

    def insert(self, key):
        if self.key == key:
            return False
        if self.key > key:
            if self.left == None:
                self.left = Node(key, self)
                self.left.color = 1
                self.left.insert_case2()
                return True
            return self.left.insert(key)
        if self.right == None:
            self.right = Node(key, self)
            self.right.color = 1
            self.right.insert_case2()
            return True
        return self.right.insert(key)