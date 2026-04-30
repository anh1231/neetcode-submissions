class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_freq = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            k_freq[i] += 1
        for key, val in k_freq.items():
            freq[val].append(key)
        final = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final) == k:
                    return final
        