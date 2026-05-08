from main import Solution

def test():
    s = Solution()

    assert s.suggestedProducts(["apple","banana"], "z") == [[]]
    assert s.suggestedProducts(["bags","baggage"], "bags")[-1] == ["bags"]

    print("All tests passed!")

if __name__ == "__main__":
    test()
