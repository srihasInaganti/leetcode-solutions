from main import Solution

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def build(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for v in arr[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def test():
    s = Solution()

    head1 = build([1,2,3,4,5])
    assert to_list(s.oddEvenList(head1)) == [1,3,5,2,4]

    head2 = build([2,1,3,5,6,4,7])
    assert to_list(s.oddEvenList(head2)) == [2,3,6,7,1,5,4]

    head3 = build([])
    assert to_list(s.oddEvenList(head3)) == []

    head4 = build([1])
    assert to_list(s.oddEvenList(head4)) == [1]

    print("All tests passed!")

if __name__ == "__main__":
    test()
