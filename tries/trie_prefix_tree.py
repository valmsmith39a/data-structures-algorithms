

class TriePrefixTree:
    """
    Problem: Implement a Trie (Prefix Tree), #208 
    
    Description: 

    Insights: 
    1. Useful for startsWith function. 
        a. If put all words in list or hash map
            i.  Need to iterate through each word: O(n) time, n: number of words 
            ii. Need to iterate through each character of the prefix: O(m) time, m: number of characters in prefix 
            ii. Total runtime: O(n*m)
        b. If put all words in a Prefix Tree
            i. Iterate through each character of the prefix: O(m) time, number of characters in prefix 

    Time Complexity: 
    1. insert: O(n), n: length of the word 
    2. search: O(n), n: length of the word
        a. Search for each letter in children is O(1) time, perform O(n) times 
    3. startsWith: O(1)
        a. Search for each letter of prefix in children is O(1) time and perform O(n) times 

    Space Complexity: 
    1. insert: O(n)
    2. search: O(1)
    3. startsWith: O(1)
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word: str) -> bool:
        curr = self.root 

        for c in word:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return curr.endOfWord
    

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 

        for c in prefix:
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return True 

class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False
