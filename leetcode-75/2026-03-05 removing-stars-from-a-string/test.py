from main import Solution

def test():
    s = Solution()

    assert s.removeStars("leet**cod*e") == "lecoe"
    assert s.removeStars("erase*****") == ""
    assert s.removeStars("abc") == "abc"

    print("All tests passed!")

if __name__ == "__main__":
    test()
