from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)   # "any missing key auto-becomes an empty list"
        for word in strs:
            key = "".join(sorted(word))
            groups[key].append(word)   # no if-check needed! bucket auto-created
            
        return list(groups.values())
        