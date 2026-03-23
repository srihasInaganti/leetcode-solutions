from main import Solution, TreeNode

def test():
    s = Solution()

    t1 = TreeNode(1,
                  TreeNode(2, None, TreeNode(5)),
                  TreeNode(3, None, TreeNode(4)))
    assert s.rightSideView(t1) == [1,3,4]

    assert s.rightSideView(TreeNode(1)) == [1]

    assert s.rightSideView(None) == []

    print("All tests passed!")

if __name__ == "__main__":
    test()
