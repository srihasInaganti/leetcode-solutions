from main import Solution, TreeNode

def test():
    s = Solution()

    root1 = TreeNode(1, TreeNode(7, TreeNode(7), TreeNode(-8)), TreeNode(0))
    root2 = TreeNode(-100, TreeNode(-200), TreeNode(-300))

    assert s.maxLevelSum(root1) == 2
    assert s.maxLevelSum(root2) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
