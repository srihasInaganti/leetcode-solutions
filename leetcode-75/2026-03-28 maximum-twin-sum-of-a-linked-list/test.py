from main import Solution, ListNode

def test():
    s = Solution()

    head1 = ListNode(5, ListNode(4, ListNode(2, ListNode(1))))
    head2 = ListNode(1, ListNode(100000))

    assert s.pairSum(head1) == 6
    assert s.pairSum(head2) == 100001

    print("All tests passed!")

if __name__ == "__main__":
    test()
