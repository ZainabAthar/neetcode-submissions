class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) #counts occurences
        common = freq.most_common(k) #looks for the k most common elements
        result = [item for item , _ in common] #extracts values w/o freq
        return result