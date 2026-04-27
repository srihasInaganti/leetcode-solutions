from main import Solution

def test():
    s = Solution()

    assert s.calcEquation([["a","b"]], [2.0], [["x","y"]]) == [-1.0]
    assert s.calcEquation([["a","b"]], [2.0], [["a","a"]]) == [1.0]

    print("All tests passed!")

if __name__ == "__main__":
    test()
