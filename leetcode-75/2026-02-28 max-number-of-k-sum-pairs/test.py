from main import Solution

def test():
    s = Solution()

    assert s.maxOperations([1,2,3,4], 5) == 2
    assert s.maxOperations([3,1,3,4,3], 6) == 1
    assert s.maxOperations([], 5) == 0
    assert s.maxOperations([2,2,2,2], 4) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
