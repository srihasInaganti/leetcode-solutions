from main import StockSpanner

def test():
    s = StockSpanner()

    assert [s.next(x) for x in [100,90,80,70]] == [1,1,1,1]

    s = StockSpanner()
    assert [s.next(x) for x in [100,80,60,70,60,75,85]] == [1,1,1,2,1,4,6]

    print("All tests passed!")

if __name__ == "__main__":
    test()
