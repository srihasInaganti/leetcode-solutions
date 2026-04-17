from main import Solution, TreeNode

def test():
    s = Solution()

    root1 = TreeNode(1)
    assert s.longestZigZag(root1) == 0

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    assert s.longestZigZag(root2) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
