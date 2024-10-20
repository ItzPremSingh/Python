class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.left: None | TreeNode = None
        self.right: None | TreeNode = None


def treeFormatter(tree: TreeNode) -> list[int]:
    listData = []
    while True:
        listData.append(tree.right)
        listData.append(tree.left)

    return []


def extract_data(root):
    data_list = []

    def in_order_traversal(node):
        if node:
            data_list.append(node.val)
            in_order_traversal(node.left)
            # data_list.append(node.val)
            in_order_traversal(node.right)

    in_order_traversal(root)
    return data_list


class Solution:
    def isSameTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        return True


t1 = TreeNode(1)
t2 = TreeNode(1)

t1.left = TreeNode(2)
t1.right = TreeNode(3)
t1.left.left = TreeNode(4)

t2.left = TreeNode(2)
t2.right = TreeNode(3)


# print(Solution().isSameTree(t1, t2))
print(extract_data(t1))
