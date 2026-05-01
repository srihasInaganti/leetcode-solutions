from main import Solution

def test():
    s = Solution()

    assert s.totalCost([5,4,3,2,1], 1, 3) == 1
    assert s.totalCost([1,2,4,1], 3, 3) == 4

    print("All tests passed!")

if __name__ == "__main__":
    test()
