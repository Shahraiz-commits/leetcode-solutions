class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list)      # starts with empty lists
        # defaultdict(int)       # starts with 0 for counts
        # defaultdict(set)       # starts with empty set
        # defaultdict(dict)      # nested dicts
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())
