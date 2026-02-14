from main import Solution

def test():
    s = Solution()

    assert s.pivotIndex([1,7,3,6,5,6]) == 3

    assert s.pivotIndex([1,2,3]) == -1

    assert s.pivotIndex([2,1,-1]) == 0

    assert s.pivotIndex([1]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
