class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left, right, max_len = 0, 0, 0
        dist = set()
        while right < len(s):

            if s[right] not in dist:
                dist.add(s[right])                      # process on right
                right += 1                              # expand window
                max_len = max(max_len, right - left)    # keep updating max_len
            else:
                dist.remove(s[left])                    # deduct from dist using left
                left += 1
        return max_len
