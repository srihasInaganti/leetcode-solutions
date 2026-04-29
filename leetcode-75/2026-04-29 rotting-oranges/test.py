from main import Solution

def test():
    s = Solution()

    assert s.orangesRotting([[0,2]]) == 0
    assert s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1

    print("All tests passed!")

if __name__ == "__main__":
    test()
