class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False 

class WordDictionary:
    """
    Problem: Word Dictionary 

    Key Insights: 
    1. Use Tries / Prefix Tree 
    2. Depth First Search through children nodes for wildcard character "."

    Time Complexity: 
    1. add_word: O(L), L: length of the word 
    2. search: 
        a. normal case: O(L), L: length of the word
        b. wildcard case: O(N), N: Number of TrieNodes in the tree 
    """

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        curr = self.root 
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool: 
        
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                ch = word[i]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True 
                    return False 
                else:
                    if ch not in curr.children:
                        return False 
                    curr = curr.children[ch]
            return curr.is_word
        
        return dfs(0, self.root)
    