from main import Solution
import main

pick = None

def guess(num: int) -> int:
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0

def test():
    global pick
    s = Solution()

    main.guess = guess

    pick = 6
    assert s.guessNumber(10) == 6

    pick = 1
    assert s.guessNumber(1) == 1

    pick = 10
    assert s.guessNumber(10) == 10

    print("All tests passed!")

if __name__ == "__main__":
    test()
