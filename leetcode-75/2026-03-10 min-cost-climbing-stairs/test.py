from main import Solution

def test():
    s = Solution()

    assert s.minCostClimbingStairs([10,15,20]) == 15
    assert s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
    assert s.minCostClimbingStairs([5,5]) == 5

    print("All tests passed!")

if __name__ == "__main__":
    test()
