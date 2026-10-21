class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.eow = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        trie = Trie()
        present = set()
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def dfs(r, c, curr, word):
            if (r < 0 or c < 0 or
                r >= n or c >= m or
                (r, c) in visited or
                board[r][c] not in curr.children):
                return 
            visited.add((r, c))
            curr = curr.children[board[r][c]]
            word += board[r][c]
            if curr.eow:
                present.add(word)
            for dr, dc in dirs:
                dfs(r + dr, c + dc, curr, word)
            visited.remove((r, c))
        for word in words:
            trie.add(word)
        for r in range(n):
            for c in range(m):
                dfs(r, c, trie.root, "")
        return list(present)
                    
                        
        