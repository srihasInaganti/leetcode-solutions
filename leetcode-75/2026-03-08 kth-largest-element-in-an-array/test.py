from main import Solution

def test():
    s = Solution()

    assert s.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert s.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert s.findKthLargest([1], 1) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
