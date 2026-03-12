from main import Solution

def test():
    s = Solution()

    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
