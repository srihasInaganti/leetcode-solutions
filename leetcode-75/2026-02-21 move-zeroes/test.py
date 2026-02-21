from main import Solution

def test():
    s = Solution()

    nums1 = [0,1,0,3,12]
    s.moveZeroes(nums1)
    assert nums1 == [1,3,12,0,0]

    nums2 = [0,0,0]
    s.moveZeroes(nums2)
    assert nums2 == [0,0,0]

    nums3 = [1,2,3]
    s.moveZeroes(nums3)
    assert nums3 == [1,2,3]

    nums4 = []
    s.moveZeroes(nums4)
    assert nums4 == []

    print("All tests passed!")

if __name__ == "__main__":
    test()
