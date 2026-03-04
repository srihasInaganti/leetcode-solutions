from main import Solution, TreeNode

def build_tree():
    return TreeNode(
        5,
        TreeNode(3, TreeNode(2), TreeNode(4)),
        TreeNode(6, None, TreeNode(7))
    )

def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def test():
    s = Solution()

    root = build_tree()
    root = s.deleteNode(root, 3)
    assert inorder(root) == [2, 4, 5, 6, 7]

    root = s.deleteNode(root, 5)
    assert inorder(root) == [2, 4, 6, 7]

    root = s.deleteNode(root, 7)
    assert inorder(root) == [2, 4, 6]

    print("All tests passed!")

if __name__ == "__main__":
    test()
