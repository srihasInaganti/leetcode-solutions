from main import Solution

def test():
    s = Solution()

    assert s.closeStrings("abc", "bca") == True
    assert s.closeStrings("a", "aa") == False

    print("All tests passed!")

if __name__ == "__main__":
    test()
