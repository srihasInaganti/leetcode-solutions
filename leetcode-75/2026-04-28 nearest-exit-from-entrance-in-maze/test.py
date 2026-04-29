from main import Solution

def test():
    s = Solution()

    assert s.nearestExit([["+","+","+"],["+",".","+"],["+","+","+"]], [1,1]) == -1
    assert s.nearestExit([[".",".","."],[".",".","."],[".",".","."]], [1,1]) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
