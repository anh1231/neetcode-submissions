class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            alphabet = [0] * 26
            for l in s:
                alphabet[(ord(l)-ord('a'))] += 1
            anagrams[tuple(alphabet)].append(s)
        return list(anagrams.values())