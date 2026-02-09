from main import Solution

def test():
    s = Solution()

    assert s.mergeAlternately("", "") == ""

    assert s.mergeAlternately("", "abc") == "abc"

    assert s.mergeAlternately("xyz", "") == "xyz"

    assert s.mergeAlternately("ab", "wxyz") == "awbxyz"

    print("All tests passed!")


if __name__ == "__main__":
    test()