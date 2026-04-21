from main import Solution

def test():
    s = Solution()

    assert s.longestSubarray([1,1,1,1]) == 3
    assert s.longestSubarray([1]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
