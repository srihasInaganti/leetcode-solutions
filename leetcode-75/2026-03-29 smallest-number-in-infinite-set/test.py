from main import SmallestInfiniteSet

def test():
    s = SmallestInfiniteSet()

    assert s.popSmallest() == 1
    assert s.popSmallest() == 2
    s.addBack(1)
    assert s.popSmallest() == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
