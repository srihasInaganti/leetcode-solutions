from main import Solution

def test():
    s = Solution()

    assert s.largestAltitude([-5,1,5,0,-7]) == 1
    assert s.largestAltitude([-4,-3,-2]) == 0
    assert s.largestAltitude([3]) == 3
    assert s.largestAltitude([]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
