class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        buckets = [[] for x in range(len(nums) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets) - 1, 0 , -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
