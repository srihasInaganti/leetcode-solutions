# Approach: Nested dictionaries representing trie nodes
# Time Complexity: O(n) per operation
# Space Complexity: O(total characters inserted)
# Edge Cases: Empty string search, prefix not present

class Trie:

    def __init__(self):
        self.root = {}
        
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

        curr["*"] = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        return "*" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]

        return True
