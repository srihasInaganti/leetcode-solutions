from main import Solution

def test():
    s = Solution()

    assert s.longestCommonSubsequence("", "abc") == 0
    assert s.longestCommonSubsequence("abc", "def") == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
