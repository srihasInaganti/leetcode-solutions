from main import Solution

def test():
    s = Solution()

    assert s.increasingTriplet([1,2]) == False
    assert s.increasingTriplet([5,4,3,2,1]) == False

    print("All tests passed!")

if __name__ == "__main__":
    test()
