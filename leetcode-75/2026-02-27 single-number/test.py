from main import Solution

def test():
    s = Solution()

    assert s.singleNumber([2,2,1]) == 1
    assert s.singleNumber([4,1,2,1,2]) == 4
    assert s.singleNumber([1]) == 1
    assert s.singleNumber([-1,-1,-2]) == -2

    print("All tests passed!")

if __name__ == "__main__":
    test()
