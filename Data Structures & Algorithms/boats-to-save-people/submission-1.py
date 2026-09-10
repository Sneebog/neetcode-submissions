class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        people.sort()
        #sorted list
        l = 0
        r = len(people) - 1
        count = 0            
        while l < r:    
            # print(people[l], l)
            # print(people[r], r)
            diff = people[l] + people[r]
            if diff <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            count += 1
        if l == r:
            count += 1
        return count