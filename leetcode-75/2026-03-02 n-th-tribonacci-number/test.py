from main import Solution

def test():
    s = Solution()

    assert s.tribonacci(0) == 0
    assert s.tribonacci(1) == 1
    assert s.tribonacci(2) == 1
    assert s.tribonacci(3) == 2
    assert s.tribonacci(4) == 4
    assert s.tribonacci(5) == 7
    assert s.tribonacci(10) == 149

    print("All tests passed!")

if __name__ == "__main__":
    test()
