class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        ans = []
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        for key,val in count.items():
            if val > len(nums)//3:
                ans.append(key)
        return ans
        