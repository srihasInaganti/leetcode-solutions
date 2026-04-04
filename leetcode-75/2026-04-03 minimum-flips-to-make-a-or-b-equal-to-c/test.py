from main import Solution

def test():
    s = Solution()

    assert s.minFlips(2,6,5) == 3
    assert s.minFlips(4,2,7) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
