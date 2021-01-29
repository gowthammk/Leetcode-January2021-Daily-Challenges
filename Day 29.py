# Vertical Order Traversal of a Binary Tree
#
# Solution
# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
#
# For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1)
# and (x + 1, y - 1) respectively.
#
# The vertical order traversal of a binary tree is a list of non-empty reports for each unique
# x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate.
# The report should be primarily sorted by y-coordinate from highest y-coordinate to lowest.
# If any two nodes have the same y-coordinate in the report, the node with the smaller value
# should appear earlier.
#
# Return the vertical order traversal of the binary tree.
#
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
# The node with value 9 occurs at position (-1, -1).
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
# The node with value 20 occurs at position (1, -1).
# The node with value 7 occurs at position (2, -2).
# Example 2:
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: The node with value 5 and the node with value 6 have the same position according
# to the given scheme.
# However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def bfs(root, x, y):
            if not root:
                return
            res.append(((x, y), root.val))
            bfs(root.left, x - 1, y + 1)
            bfs(root.right, x + 1, y + 1)

        bfs(root, 0, 0)
        res.sort()
        print(res)
        groups = collections.defaultdict(list)
        for k, v in res:
            x, _ = k
            groups[x].append(v)
        ans = []
        for k in sorted(list(groups.keys())):
            ans.append(groups[k])

        return ans