from main import Solution

def test():
    s = Solution()

    assert sorted(s.combinationSum3(3, 7)) == sorted([[1,2,4]])
    assert sorted(s.combinationSum3(3, 9)) == sorted([[1,2,6],[1,3,5],[2,3,4]])

    print("All tests passed!")

if __name__ == "__main__":
    test()
