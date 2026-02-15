from main import Solution

def test():
    s = Solution()

    assert s.uniqueOccurrences([1,2,2,1,1,3]) is True

    assert s.uniqueOccurrences([1,2]) is False

    assert s.uniqueOccurrences([3,3,3,3]) is True

    assert s.uniqueOccurrences([]) is True

    print("All tests passed!")

if __name__ == "__main__":
    test()

