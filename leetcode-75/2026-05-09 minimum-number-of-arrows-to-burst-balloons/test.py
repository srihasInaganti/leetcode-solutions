from main import Solution

def test():
    s = Solution()

    assert s.findMinArrowShots([[1,5],[2,6],[3,7]]) == 1
    assert s.findMinArrowShots([[1,2],[3,4],[5,6]]) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test()
