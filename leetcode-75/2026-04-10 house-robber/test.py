from main import Solution

def test():
    s = Solution()

    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12

    print("All tests passed!")

if __name__ == "__main__":
    test()
