class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = ''.join(sorted(s))
            res[tuple(count)].append(s)
        return res.values()
            



      
            
        