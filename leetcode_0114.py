# pip install networkx matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# region Visualize tree
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.val, pos=(x, y))
        if node.left:
            graph.add_edge(node.val, node.left.val)
            add_edges(graph, node.left, pos, x - 1 / layer, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            add_edges(graph, node.right, pos, x + 1 / layer, y - 1, layer + 1)


def draw_tree(root):
    graph = nx.DiGraph()
    pos = {}
    add_edges(graph, root, pos)
    pos = nx.get_node_attributes(graph, 'pos')

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, with_labels=True, node_size=2000,
            node_color="lightblue", edge_color="gray")
    plt.show()
# endregion


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.prev = None

        def navigate(node: Optional[TreeNode]):
            if not node:
                return

            navigate(node.right)
            navigate(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node
            # draw_tree(root)

        navigate(root)


s = Solution()

# Example Tree
root = TreeNode(1,
                TreeNode(2, TreeNode(3), TreeNode(4)),
                TreeNode(5, None, TreeNode(6)))

s.flatten(root)
draw_tree(root)
