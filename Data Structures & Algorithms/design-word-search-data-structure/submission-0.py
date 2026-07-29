class TrieNode():
    def __init__(self):
        self.characters = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
        cur.endOfWord = True        


    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for character in cur.characters.values():
                        if dfs(i + 1, character):
                            return True
                    return False
                else:
                    if c not in cur.characters:
                        return False
                    cur = cur.characters[c]
            return cur.endOfWord

        return dfs(0, self.root)   
        
