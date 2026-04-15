from main import Solution

def test():
    s = Solution()

    assert s.isSubsequence("", "ahbgdc") == True
    assert s.isSubsequence("abcd", "abc") == False

    print("All tests passed!")

if __name__ == "__main__":
    test()
