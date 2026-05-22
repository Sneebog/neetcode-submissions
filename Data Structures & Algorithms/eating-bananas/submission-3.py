import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        num_piles = len(piles)
        r_k = piles[-1]
        l_k = 1
        lowest_k = r_k

        while l_k <= r_k:
            m_k = l_k + (r_k - l_k) // 2
            flag = True
            count = 0
            h_total = 0

            while flag and count < num_piles:
                h_total += math.ceil(piles[count] / m_k)
                if h_total > h:
                    flag = not(flag)
                count += 1

            if flag:
                lowest_k = min(lowest_k, m_k)
                r_k = m_k - 1
            else:
                l_k = m_k  + 1


        return lowest_k
