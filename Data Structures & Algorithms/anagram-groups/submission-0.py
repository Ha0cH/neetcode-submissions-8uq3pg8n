class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            key = tuple(sorted(s))
            if key not in seen:
                seen[key] = []
            seen[key].append(s)

        return list(seen.values())