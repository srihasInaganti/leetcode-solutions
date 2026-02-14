from main import Solution

def test():
    s = Solution()

    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([0,1,2,3]) == [6,0,0,0]
    assert s.productExceptSelf([0,0]) == [0,0]
    assert s.productExceptSelf([5]) == [1]

    print("All tests passed!")

if __name__ == "__main__":
    test()
