import unittest
import rbtree

def makect():
    ct = rbtree.RBTree()
    ct.root = rbtree.Node(3)
    ct.root.left = rbtree.Node(1, ct.root)
    ct.root.right = rbtree.Node(5, ct.root)
    ct.root.left.left = rbtree.Node(0, ct.root.left)
    ct.root.left.right = rbtree.Node(2, ct.root.left)
    ct.root.right.left = rbtree.Node(4, ct.root.right)
    ct.root.right.right = rbtree.Node(7, ct.root.right)
    ct.root.right.right.left = rbtree.Node(6, ct.root.right.right)
    ct.root.right.right.right = rbtree.Node(8, ct.root.right.right)
    ct.root.right.right.right.right = rbtree.Node(9, ct.root.right.right.right)
    return ct

def only_keys_comparator(t1, t2):
    if t1.key == t2.key:
        return True
    return False

def tree_compare(t1:rbtree.Node, t2:rbtree.Node, comparator=only_keys_comparator):
    if t1 == None or t2 == None:
        return t1 == t2
    if not tree_compare(t1.left, t2.left):
        return False
    if not tree_compare(t1.right, t2.right):
        return False
    return comparator(t1, t2)

class TestRBTree(unittest.TestCase):
    def test_creation(self):
        t = rbtree.RBTree()
        self.assertNotEqual(t, None)
    
    def test_insert_one(self):
        t = rbtree.RBTree()
        t.insert(2)
        self.assertEqual(t.root.key, 2)
    
    def test_find_none(self):
        t = rbtree.RBTree()
        self.assertFalse(t.find(2))

    def test_find_one(self):
        t = rbtree.RBTree()
        t.insert(2)
        self.assertTrue(t.find(2))

    def test_insert_many(self):
        t = rbtree.RBTree()
        for i in range(10):
            t.insert(i)
        ct = makect()
        self.assertTrue(tree_compare(t.root, ct.root))

    def test_find_many(self):
        t = rbtree.RBTree()
        for i in range(10):
            t.insert(i)
        for i in range(10):
            self.assertTrue(t.find(i))
    
    def test_find_many2(self):
        t = rbtree.RBTree()
        for i in range(10, 0, -1):
            t.insert(i)
        for i in range(1, 11):
            self.assertTrue(t.find(i))

    def test_delete_none(self):
        t = rbtree.RBTree()
        self.assertFalse(t.delete(2))

    def test_delete_leaf(self):
        t = rbtree.RBTree()
        for i in range(10):
            t.insert(i)
        self.assertTrue(t.delete(9))
        ct = makect()
        ct.root.right.right.right.right = rbtree.Node(None, ct.root.right.right.right)
        self.assertTrue(tree_compare(t.root, ct.root))
    
    def test_delete_many(self):
        t = rbtree.RBTree()
        for i in range(10):
            t.insert(i)
        for i in range(5, 10):
            self.assertTrue(t.delete(i))
        ct = makect()
        ct.root.right = rbtree.Node(4, ct.root)
        self.assertTrue(tree_compare(t.root, ct.root))


if __name__ == '__main__':
    unittest.main()