class Trie:

    def __init__(self):
        self.trie = {}
        self.end_of_word = "#"


    def insert(self, word: str) -> None:
        node = self.trie
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word


    def search(self, word: str) -> bool:
        node = self.trie
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Time complexity: O(n), where n is the length of the word
# Space complexity: O(n)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

import unittest

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_trie(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.startsWith("app"))
        self.assertFalse(self.trie.search("orange"))
        self.assertFalse(self.trie.startsWith("orange"))

if __name__ == '__main__':
    unittest.main()
