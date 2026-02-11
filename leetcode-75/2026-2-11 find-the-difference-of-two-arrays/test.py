from main import Solution

def test():
    s = Solution()

    assert sorted([sorted(x) for x in s.findDifference([1,2,3], [2,4,6])]) == sorted([[1,3],[4,6]])

    assert sorted([sorted(x) for x in s.findDifference([1,1,2], [1,1,2])]) == sorted([[],[]])

    assert sorted([sorted(x) for x in s.findDifference([], [1,2])]) == sorted([[],[1,2]])

    assert sorted([sorted(x) for x in s.findDifference([1,2,3], [1,2,3])]) == sorted([[],[]])

    print("All tests passed!")

if __name__ == "__main__":
    test()
