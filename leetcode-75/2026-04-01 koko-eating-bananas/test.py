from main import Solution

def test():
    s = Solution()

    assert s.minEatingSpeed([3,6,7,11], 8) == 4
    assert s.minEatingSpeed([30,11,23,4,20], 5) == 30

    print("All tests passed!")

if __name__ == "__main__":
    test()
