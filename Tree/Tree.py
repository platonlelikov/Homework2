from dataclasses import dataclass


@dataclass
class Tree:
    data: int
    left = None
    right = None


def tree_from_list(nodes):
    int_nodes = [None if i == '' else int(i) for i in nodes]
    root = Tree(int_nodes[0])
    def roots(i=0):
        if  i < len(int_nodes) and int_nodes[i] is not None:
            root = Tree(int_nodes[i])
            root.left = roots(2*i+1)
            root.right = roots(2*i+2)
            return root
        return None
    return roots()


def find_way(root, sum):
    if not root:
        return []
    if root.data == sum:
        return [root.data]
    left_way=find_way(root.left, sum - root.data)
    if left_way:
        return [root.data] + left_way
    right_way=find_way(root.right, sum - root.data)
    if right_way:
        return [root.data] + right_way
    return[]