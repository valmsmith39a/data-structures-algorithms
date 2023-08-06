from typing import List

class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False 

    def add_word(self, word):

        curr = self 

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.is_word = True 

class WordSearchTwo:

    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        for w in words:
            root.add_word(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):

            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
                (r, c) in visited or 
                board[r][c] not in node.children):
                return 
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
             
            if node.is_word:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)
            
