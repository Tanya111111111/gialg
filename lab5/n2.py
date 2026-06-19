#104
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)
        return 1 + max(depth_left, depth_right)