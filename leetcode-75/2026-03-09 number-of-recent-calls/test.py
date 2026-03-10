from main import RecentCounter

def test():
    r = RecentCounter()

    assert r.ping(1) == 1
    assert r.ping(100) == 2
    assert r.ping(3001) == 3
    assert r.ping(3002) == 3

    print("All tests passed!")

if __name__ == "__main__":
    test()
