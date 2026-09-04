# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            level=[]
            for _ in range(len(q)):
                i = q.popleft()
                level.append(i.val)
                if i.left:
                    q.append(i.left)
                if i.right:
                    q.append(i.right)
            ans.append(level)
        return ans
