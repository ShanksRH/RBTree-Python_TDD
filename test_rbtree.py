import unittest
import rbtree

class TestRBTree(unittest.TestCase):
    def test_creation(self):
        t = rbtree.RBTree()
        self.assertNotEqual(t, None)
    
    def test_insert_one(self):
        t = rbtree.RBTree()
        t.insert(2)
        self.assertEqual(t.root.key, 2)
    
    def test_find_one(self):
        t = rbtree.RBTree()
        t.insert(2)
        self.assertEqual(t.find(2), True)

if __name__ == '__main__':
    unittest.main()