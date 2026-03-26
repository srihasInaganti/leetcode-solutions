from main import Solution

def test():
    s = Solution()

    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test()
