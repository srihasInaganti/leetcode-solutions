from main import Solution

def test():
    s = Solution()

    assert s.findPeakElement([1]) == 0
    assert s.findPeakElement([1,2,3,1]) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
