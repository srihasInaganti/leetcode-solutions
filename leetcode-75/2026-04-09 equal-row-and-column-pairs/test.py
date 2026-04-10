from main import Solution

def test():
    s = Solution()

    assert s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert s.equalPairs([[1,1],[1,1]]) == 4

    print("All tests passed!")

if __name__ == "__main__":
    test()
