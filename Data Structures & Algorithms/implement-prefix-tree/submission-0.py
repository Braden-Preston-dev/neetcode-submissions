class TrieNode:
    def __init__(self):
        self.children = {} 
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.end_of_word = True


    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.children: return False
            cur = cur.children[w]
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children: return False
            cur = cur.children[c]
        return True