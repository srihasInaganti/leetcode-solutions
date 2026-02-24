from main import Solution

def test():
    s = Solution()

    assert s.countBits(0) == [0]
    assert s.countBits(1) == [0,1]
    assert s.countBits(2) == [0,1,1]
    assert s.countBits(5) == [0,1,1,2,1,2]

    print("All tests passed!")

if __name__ == "__main__":
    test()
