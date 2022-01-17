class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


def is_leaf(root):
    return root and not root.left and not root.right


def left_leaves_helper(root):
    sums = 0
    if root.left:
        if is_leaf(root.left):
            sums += root.left.val
        else:
            sums += left_leaves_helper(root.left)

    if root.right:
        sums += left_leaves_helper(root.right)

    return sums


def sum_of_left_leaves(root):
    if not root:
        return 0

    return left_leaves_helper(root)


def input_binary_tree():
    input_values = input().split()
    index = 0
    num_nodes = int(input_values[index])
    index += 1
    if (num_nodes == 0):
        return None

    nodes = []
    current_parent_index = 0

    root = TreeNode(int(input_values[index]))
    index += 1
    nodes.append(root)

    for i in range(1, num_nodes, 2):
        left_val = int(input_values[index])
        index += 1
        if (left_val != -1):
            left = TreeNode(left_val)
            nodes.append(left)
            nodes[current_parent_index].left = left

        right_val = int(input_values[index])
        index += 1
        if (right_val != -1):
            right = TreeNode(right_val)
            nodes.append(right)
            nodes[current_parent_index].right = right

        current_parent_index += 1

    return root

root = input_binary_tree()
sum = sum_of_left_leaves(root)

print(sum)