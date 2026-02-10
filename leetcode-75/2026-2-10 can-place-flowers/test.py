from main import Solution

def test():
    s = Solution()

    assert s.canPlaceFlowers([1,0,0,0,1], 1) is True

    assert s.canPlaceFlowers([1,0,0,0,1], 2) is False

    assert s.canPlaceFlowers([0], 1) is True

    assert s.canPlaceFlowers([0,0,0], 2) is True

    assert s.canPlaceFlowers([1,1,1], 0) is True

    print("All tests passed!")

if __name__ == "__main__":
    test()
