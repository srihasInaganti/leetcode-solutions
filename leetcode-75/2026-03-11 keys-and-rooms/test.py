from main import Solution

def test():
    s = Solution()

    assert s.canVisitAllRooms([[1],[2],[3],[]]) is True
    assert s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) is False
    assert s.canVisitAllRooms([[]]) is True

    print("All tests passed!")

if __name__ == "__main__":
    test()
