class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people)-1
        ans = 0
        while l < r:
            if people[r] + people[l] <= limit:
                ans += 1
                r -= 1
                l += 1
            if people[r] + people[l] > limit:
                r -= 1
        return len(people)-(ans)

        