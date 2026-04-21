from main import Solution

def test():
    s = Solution()

    chars1 = ["a"]
    assert s.compress(chars1) == 1

    chars2 = ["a","b","c"]
    assert s.compress(chars2) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test()
