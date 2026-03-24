from main import Solution

def test():
    s = Solution()

    assert s.asteroidCollision([5,10,-5]) == [5,10]
    assert s.asteroidCollision([8,-8]) == []

    print("All tests passed!")

if __name__ == "__main__":
    test()
