import unittest 
from trie_prefix_tree import TriePrefixTree

class TestTriePrefixTree(unittest.TestCase):

    def setUp(self):
        self.trie = TriePrefixTree()

    def test_insert(self):
        self.trie.insert("bear")
        self.assertTrue('b' in self.trie.root.children)
        self.assertFalse(self.trie.root.endOfWord)
        self.assertTrue('e' in self.trie.root.children['b'].children)
        self.assertFalse(self.trie.root.children['b'].endOfWord)

        self.trie.insert("be")
        self.assertTrue(self.trie.root.children['b'].children['e'].endOfWord)

    def test_search(self):
        self.trie.insert("bear")
        self.trie.insert("be")
        self.assertTrue(self.trie.search("bear"))
        self.assertTrue(self.trie.search("be"))
        self.assertFalse(self.trie.search("bea"))
        self.assertFalse(self.trie.search("beare"))

    def test_startsWith(self):
        self.trie.insert("bear")
        self.assertTrue(self.trie.startsWith("b"))
        self.assertTrue(self.trie.startsWith("be"))
        self.assertTrue(self.trie.startsWith("bea"))
        self.assertTrue(self.trie.startsWith("bear"))
        self.assertFalse(self.trie.startsWith("beare"))

if __name__ == "__main__":
    unittest.main()
