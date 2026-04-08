from main import Solution

def test():
    s = Solution()

    assert s.maxScore([1,3,3,2], [2,1,3,4], 3) == 12
    assert s.maxScore([4,2,3,1,1], [7,5,10,9,6], 1) == 30

    print("All tests passed!")

if __name__ == "__main__":
    test()
