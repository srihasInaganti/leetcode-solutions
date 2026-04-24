from main import Solution

def test():
    s = Solution()

    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("12[a]") == "aaaaaaaaaaaa"

    print("All tests passed!")

if __name__ == "__main__":
    test()
