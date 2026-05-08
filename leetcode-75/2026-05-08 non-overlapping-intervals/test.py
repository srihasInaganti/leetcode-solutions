from main import Solution

def test():
    s = Solution()

    assert s.eraseOverlapIntervals([[1,2],[2,3],[3,4]]) == 0
    assert s.eraseOverlapIntervals([[1,4],[2,4],[3,4]]) == 2

    print("All tests passed!")

if __name__ == "__main__":
    test()
