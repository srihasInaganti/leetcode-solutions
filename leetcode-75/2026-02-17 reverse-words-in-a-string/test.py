from main import Solution

def test():
    s = Solution()

    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good   example") == "example good a"
    assert s.reverseWords("") == ""

    print("All tests passed!")

if __name__ == "__main__":
    test()
