from main import Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test():
    s = Solution()

    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(7))

    assert s.searchBST(root, 2).val == 2
    assert s.searchBST(root, 5) is None
    assert s.searchBST(None, 1) is None
    assert s.searchBST(TreeNode(1), 1).val == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
