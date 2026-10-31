class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        nums_list = seen.items()
        nums_list_desc = sorted(nums_list, key = lambda nums_list: nums_list[1] , reverse = True)
        a = nums_list_desc[:k]

        result = []
        for pair in a:
            result.append(pair[0])
        return result