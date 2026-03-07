from main import Solution

def test():
    s = Solution()

    assert s.maxVowels("abciiidef", 3) == 3
    assert s.maxVowels("aeiou", 2) == 2
    assert s.maxVowels("leetcode", 3) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
