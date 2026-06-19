#102
class Solution(object):
    def levelOrder(self, root):
        levels = []

        def traverse(curr, depth):
            if curr is None:
                return
            if len(levels) == depth:
                levels.append([])
            levels[depth].append(curr.val)
            traverse(curr.left, depth + 1)
            traverse(curr.right, depth + 1)

        traverse(root, 0)
        return levels