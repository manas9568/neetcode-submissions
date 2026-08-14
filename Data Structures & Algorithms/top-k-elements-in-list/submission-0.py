class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if n in map:
                map[n] += 1
            else:
                map[n] = 1
        arr = [[] for i in range(len(nums)+1)]
        for key,value in map.items():
            arr[value].append(key)
        ans = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i]:
                ans.extend(arr[i])
        return ans[:k]






        