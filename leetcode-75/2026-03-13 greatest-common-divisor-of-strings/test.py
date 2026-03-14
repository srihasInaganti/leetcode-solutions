from main import Solution

def test():
    s = Solution()

    assert s.gcdOfStrings("ABCABC", "ABC") == "ABC"
    assert s.gcdOfStrings("ABABAB", "ABAB") == "AB"
    assert s.gcdOfStrings("LEET", "CODE") == ""

    print("All tests passed!")

if __name__ == "__main__":
    test()
