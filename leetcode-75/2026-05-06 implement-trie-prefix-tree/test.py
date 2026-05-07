from main import Trie

def test():
    t = Trie()

    assert t.search("") == False

    t.insert("apple")
    assert t.startsWith("appx") == False

    print("All tests passed!")

if __name__ == "__main__":
    test()
