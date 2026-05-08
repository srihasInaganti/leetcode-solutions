from typing import List

# Approach: Sort products and scan for matching prefixes
# Time Complexity: O(n * m)
# Space Complexity: O(1)
# Edge Cases: No matching products, fewer than 3 matches

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        st = ""
        out = []

        for c in searchWord:
            st += c
            curr = []
            for p in products:
                if p.startswith(st):
                    curr.append(p)
                if len(curr) == 3:
                    break

            out.append(curr)
        return out
