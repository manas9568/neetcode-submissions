class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = set(nums1)
        map2 = set(nums2)
        res = []
        for ele in map2:
            if ele in map1:
                res.append(ele)
        return res
        