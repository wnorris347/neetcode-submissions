class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_ops = 100
        i = 0
        j = k
        while j <= len(blocks):
            min_ops = min(min_ops, blocks[i:j].count("W"))
            i += 1
            j += 1
        return min_ops
