from main import Solution

def test():
    s = Solution()

    assert sorted(s.letterCombinations("23")) == sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"])
    assert s.letterCombinations("") == []

    print("All tests passed!")

if __name__ == "__main__":
    test()
