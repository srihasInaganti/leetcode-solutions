from main import Solution

def test():
    s = Solution()

    assert s.numTilings(1) == 1
    assert s.numTilings(2) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
