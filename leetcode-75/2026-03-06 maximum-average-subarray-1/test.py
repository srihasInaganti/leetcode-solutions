from main import Solution

def test():
    s = Solution()

    assert s.findMaxAverage([1,12,-5,-6,50,3], 4) == 12.75
    assert s.findMaxAverage([5], 1) == 5.0
    assert s.findMaxAverage([-1,-2,-3,-4], 2) == -1.5

    print("All tests passed!")

if __name__ == "__main__":
    test()
