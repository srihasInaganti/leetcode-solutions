from main import Solution

def test():
    s = Solution()

    assert s.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert s.dailyTemperatures([30,30,30]) == [0,0,0]

    print("All tests passed!")

if __name__ == "__main__":
    test()
