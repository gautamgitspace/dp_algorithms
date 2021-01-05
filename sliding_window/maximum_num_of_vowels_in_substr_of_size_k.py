class Solution(object):
    def maxVowels(self, s, k):
        """
        using while and explicit
        increment condition

        106 / 106 test cases passed.
        Status: Accepted
        Runtime: 256 ms
        Memory Usage: 14.6 MB
        """
        L, R, count = 0, 0, 0
        best = count
        while R < len(s):
            count += s[R] in 'aeiou'
            if R - L + 1 < k:
                R += 1
            elif R - L + 1 == k:
                best = max(count, best)
                R += 1
            if R - L + 1 > k:
                count -= s[L] in 'aeiou'
                L += 1
        return best

    def maxVowels(self, s, k):
        """
        using for and R as idx increment

        106 / 106 test cases passed.
        Status: Accepted
        Runtime: 228 ms
        Memory Usage: 14.7 MB
        """

        L = vowels = best = 0
        
        for R, char in enumerate(s):
            vowels += char in 'aeiou'
            if R - L + 1 > k:
                vowels -= s[L] in 'aeiou'
                L += 1
            if R - L + 1 == k:
                best = max(vowels, best)
        return best
