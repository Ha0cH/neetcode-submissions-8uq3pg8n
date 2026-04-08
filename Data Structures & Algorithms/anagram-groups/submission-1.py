class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)

            if key not in seen:
                seen[key] = []

            seen[key].append(s)

        return list(seen.values())