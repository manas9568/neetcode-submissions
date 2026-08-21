class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ele in s:
            freq[ele] = freq.get(ele,0) + 1
        ans = ""
        for key, val in freq.items():
            if val == 1:
                ans = key
                break
        if ans:
            for i in range(len(s)):
                if s[i] == ans:
                    return i
        return -1
        
        