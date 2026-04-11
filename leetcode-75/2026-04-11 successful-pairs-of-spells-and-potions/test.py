from main import Solution

def test():
    s = Solution()

    assert s.successfulPairs([5,1,3], [1,2,3,4,5], 7) == [4,0,3]
    assert s.successfulPairs([3,1,2], [8,5,8], 16) == [2,0,2]

    print("All tests passed!")

if __name__ == "__main__":
    test()
