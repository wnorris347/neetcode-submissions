class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        curr = root
        stack = []
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            i += 1
            if i == k:
                return node.val
            curr = node.right