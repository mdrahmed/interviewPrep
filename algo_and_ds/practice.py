class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.end

    def searchPre(self, pre):
        curr = self.root
        for c in pre:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

