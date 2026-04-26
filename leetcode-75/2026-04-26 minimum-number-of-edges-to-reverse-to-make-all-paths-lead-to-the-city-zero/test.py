from main import Solution

def test():
    s = Solution()

    assert s.minReorder(1, []) == 0
    assert s.minReorder(3, [[1,0],[2,0]]) == 0

    print("All tests passed!")

if __name__ == "__main__":
    test()
