from main import Solution

def test():
    s = Solution()

    assert s.kidsWithCandies([], 3) == []

    assert s.kidsWithCandies([2,2,2], 1) == [True, True, True]

    assert s.kidsWithCandies([2,3,5], 0) == [False, False, True]

    assert s.kidsWithCandies([4], 2) == [True]

    print("All tests passed!")

if __name__ == "__main__":
    test()
