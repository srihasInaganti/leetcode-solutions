from main import Solution

def test():
    s = Solution()

    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("", "abc") == 3

    print("All tests passed!")

if __name__ == "__main__":
    test()
