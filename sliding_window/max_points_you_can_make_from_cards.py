class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        mixed draw : conidering draw
        from either side. start from
        the fixed window  size of  k
        from the right end. keep best
        as sum of cardPoints[R:] and
        keep updating it at each iter
        
        [1 2 3 4 (5 6 1)]
        [1) 2 3 4 5 (6 1]        
        [1 2) 3 4 5 6 (1]
        [(1 2 3) 4 5 6 1]
        """
        size = len(cardPoints)
        L, R = 0, size - k
        total = sum(cardPoints[R:])
        best = total
        
        for _ in range(k):
            # include add L (add) exclude R (subtract)
            total += cardPoints[L] - cardPoints[R]
            best = max(best, total)
            # move window
            L += 1
            R += 1
        return best
    
    def maxScore2(self, cardPoints, k):
        """
        would work for only one sided draw
        """
        pointsL = pointsR = 0
        L, R = 0, len(cardPoints) - 1
        
        while L < k:
            pointsL += cardPoints[L]
            L += 1
        
        while R >= len(cardPoints) - k:
            pointsR += cardPoints[R]
            R -= 1
        
        return max(pointsL, pointsR)
