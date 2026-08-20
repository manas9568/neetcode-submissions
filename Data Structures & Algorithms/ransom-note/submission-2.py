class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_freq = {}
        for mag in magazine:
            mag_freq[mag] = mag_freq.get(mag,0) + 1
        ran_freq = {}
        for ran in ransomNote:
            ran_freq[ran] = ran_freq.get(ran,0) + 1
        for key,val in ran_freq.items():
            if val > mag_freq.get(key,0):
                return False
        return True

        