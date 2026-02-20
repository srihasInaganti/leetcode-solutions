from main import Solution

def test():
    s = Solution()

    assert s.reverseVowels("hello") == "holle"
    assert s.reverseVowels("leetcode") == "leotcede"
    assert s.reverseVowels("aA") == "Aa"
    assert s.reverseVowels("bcdfg") == "bcdfg"

    print("All tests passed!")

if __name__ == "__main__":
    test()
