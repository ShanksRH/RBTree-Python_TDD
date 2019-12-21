class RBTree:
    def __init__(self):
        self.root = None
        pass
    
    def find(self, key):
        if self.root == None:
            return None
        return self.root.find(key)
    
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
            return True
        res = self.root.insert(key)
        while self.root.parent != None:
            self.root = self.root.parent
        return res
    
    def delete(self, key):
        if self.root == None:
            return False
        res = self.root.delete(key)
        while self.root.parent != None:
            self.root = self.root.parent
        if self.root.key == None:
            self.root = None
        return res

class Node:
    color = 0

    def __init__(self, key=None, parent=None):
        self.parent, self.key = parent, key
        if key != None:   
            self.left, self.right = Node(None, self), Node(None, self)
        else:
            self.left, self.right = None, None

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
    
    def bro(self):
        if self.parent.left == self:
            return self.parent.right
        return self.parent.left
    
    def reconnect(self, other):
        other.parent = self.parent
        if self.parent != None:
            if self.parent.left == self:
                self.parent.left = other
            else:
                self.parent.right = other

    def rotate_right(self):
        pivot = self.left
        self.reconnect(pivot)
        self.parent = pivot
        self.left = pivot.right
        if pivot.right != None:
            pivot.right.parent = self
        pivot.right = self

    def rotate_left(self):
        pivot = self.right
        self.reconnect(pivot)
        self.parent = pivot
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
        n = self
        if self == self.parent.right and self.parent == g.left:
            self.parent.rotate_left()
            n = self.left
        elif self == self.parent.left and self.parent == g.right:
            self.parent.rotate_right()
            n = self.right
        n.insert_case5()

    def insert_case5(self):
        g = self.grandparent()
        self.parent.color, g.color = 0, 1
        if self == self.parent.left and self.parent == g.left:
            g.rotate_right()
        else:
            g.rotate_left()
    
    def delete_case1(self):
        if self.parent != None:
            self.delete_case2()
        else:
            return True
    
    def delete_case2(self):
        b = self.bro()
        if b.color == 1:
            self.parent.color = 1
            b.color = 0
            if self.parent.left == self:
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        self.delete_case3()

    def delete_case3(self):
        b = self.bro()
        if self.parent.color == 0 and b.color == 0 and \
            b.left.color == 0 and b.right.color == 0:
            b.color = 1
            self.parent.delete_case1()
        else:
            self.delete_case4()
    
    def delete_case4(self):
        b = self.bro()
        if self.parent.color == 1 and b.color == 0 and \
            b.left.color == 0 and b.right.color == 0:
            b.color = 1
            self.parent.color = 0
        else:
            self.delete_case5()
    
    def delete_case5(self):
        b = self.bro()
        if b.color == 0:
            if self == self.parent.left and \
                b.right.color == 0 and b.left.color == 1:
                b.color = 1
                b.left.color = 0
                b.rotate_right()
            elif self == self.parent.right and \
                b.left.color == 0 and b.right.color == 1:
                b.color = 1
                b.right.color = 0
                b.rotate_left()
        self.delete_case6()
    
    def delete_case6(self):
        b = self.bro()
        b.color = self.parent.color
        self.parent.color = 0
        if self == self.parent.left:
            b.right.color = 0
            self.parent.rotate_left()
        else:
            b.left.color = 0
            self.parent.rotate_right()

    def find(self, key):
        if self.key == key:
            return self
        if self.key > key:
            if self.left.key == None:
                return None
            return self.left.find(key)
        if self.right.key == None:
            return None
        return self.right.find(key)
    
    def insert(self, key):
        if self.key == key:
            return False
        if self.key > key:
            if self.left.key == None:
                self.left = Node(key, self)
                self.left.color = 1
                self.left.insert_case2()
                return True
            return self.left.insert(key)
        if self.right.key == None:
            self.right = Node(key, self)
            self.right.color = 1
            self.right.insert_case2()
            return True
        return self.right.insert(key)
    
    def delete_one_child(self):
        child = self.right
        if self.right.key == None:
            child = self.left
        self.reconnect(child)
        if self.color == 0:
            if child.color == 1:
                child.color = 0
            else:
                if child.delete_case1():
                    self.parent = child
    
    def delete(self, key):
        if self.key == key:
            ch = self
            if self.left.key != None:
                ch = self.left
                while ch.right.key != None:
                    ch = ch.right
                self.key = ch.key
            ch.delete_one_child()
            return True
        if self.key > key:
            if self.left.key == None:
                return False
            return self.left.delete(key)
        if self.right.key == None:
            return False
        return self.right.delete(key)
