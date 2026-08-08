class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.eow = True
            
    

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = [-1] * len(s)
        trie = Trie(dictionary).root
        def dfs(i):
            if i == len(s):
                return 0
            if dp[i] != -1:
                return dp[i]
            res = 1 + dfs(i + 1)
            cur = trie
            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.eow:
                    res = min(res, dfs(j + 1))
            dp[i] = res
            return res
        return dfs(0)

        