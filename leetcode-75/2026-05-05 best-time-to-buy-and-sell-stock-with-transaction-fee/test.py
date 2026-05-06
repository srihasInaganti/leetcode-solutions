from main import Solution

def test():
    s = Solution()

    assert s.maxProfit([5], 2) == 0
    assert s.maxProfit([5,4,3,2,1], 1) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
