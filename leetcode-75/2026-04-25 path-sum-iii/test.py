from main import Solution, TreeNode

def test():
    s = Solution()

    assert s.pathSum(None, 5) == 0

    root = TreeNode(5)
    assert s.pathSum(root, 5) == 1

    print("All tests passed!")

if __name__ == "__main__":
    test()
