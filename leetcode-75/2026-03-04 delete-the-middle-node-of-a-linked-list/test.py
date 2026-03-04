from main import Solution, ListNode

def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

def test():
    s = Solution()

    head = build_list([1,3,4,7,1,2,6])
    head = s.deleteMiddle(head)
    assert to_list(head) == [1,3,4,1,2,6]

    head = build_list([1,2,3,4])
    head = s.deleteMiddle(head)
    assert to_list(head) == [1,2,4]

    head = build_list([2,1])
    head = s.deleteMiddle(head)
    assert to_list(head) == [2]

    head = build_list([1])
    head = s.deleteMiddle(head)
    assert head is None

    print("All tests passed!")

if __name__ == "__main__":
    test()
