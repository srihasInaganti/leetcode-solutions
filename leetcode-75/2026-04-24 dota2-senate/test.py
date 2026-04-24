from main import Solution

def test():
    s = Solution()

    assert s.predictPartyVictory("RRR") == "Radiant"
    assert s.predictPartyVictory("RDRD") == "Radiant"

    print("All tests passed!")

if __name__ == "__main__":
    test()
