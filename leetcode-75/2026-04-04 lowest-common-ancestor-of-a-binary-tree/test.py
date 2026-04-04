from main import Solution, TreeNode

def test():
    s = Solution()

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)

    assert s.lowestCommonAncestor(root, root.left, root.right).val == 3
    assert s.lowestCommonAncestor(root, root.left, root.left.right).val == 5

    print("All tests passed!")

if __name__ == "__main__":
    test()
