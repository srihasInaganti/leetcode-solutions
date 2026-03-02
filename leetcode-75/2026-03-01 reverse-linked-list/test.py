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
    assert to_list(s.reverseList(head1)) == [5,4,3,2,1]

    head2 = build([1])
    assert to_list(s.reverseList(head2)) == [1]

    head3 = build([])
    assert to_list(s.reverseList(head3)) == []

    print("All tests passed!")

if __name__ == "__main__":
    test()
