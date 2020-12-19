class Solution(object):
    def minWindow(self, s, t):
        hash_map = dict()
        for c in t:
            if c in hash_map:
                hash_map[c] += 1
            else:
                hash_map[c] = 1

        start, end = 0, 0

        # If the minimal length doesn't change, it means there's no valid window
        min_window_length = len(s) + 1

        # Start point of the minimal window
        min_window_start = 0

        # Works as a counter of how many chars still need to be included in a window
        num_of_chars_to_be_included = len(t)

        while end < len(s):
            # If the current char is desired
            if s[end] in hash_map:
                print 'MAP HIT! ' + s[end]
                # Then we decreased the counter, if this char is a "must-have" now, in a sense of critical value
                if hash_map[s[end]] > 0:
                    print 'decrementing num_of_chars_to_be_included for ' + s[end]
                    num_of_chars_to_be_included -= 1
                    print 'num_of_chars_to_be_included ' + str(num_of_chars_to_be_included)
                # And we decrease the hash_map value
                hash_map[s[end]] -= 1

            # If the current window has all the desired chars
            while num_of_chars_to_be_included == 0:
                print "ALL HITS COMPLETED"
                # See if this window is smaller
                if end - start + 1 < min_window_length:
                    min_window_length = end - start + 1
                    print "MWL: " + str(min_window_length)
                    min_window_start = start
                    print "win start " + str(min_window_start)

                # if s[start] is desired, we need to update the hash_map value and the counter
                if s[start] in hash_map:
                    print 'incrementing map for ' + s[start] + ' from ' + str(hash_map[s[start]])
                    hash_map[s[start]] += 1
                    print 'to ' + str(hash_map[s[start]])
                    # Still, update the counter only if the current char is "critical"
                    if hash_map[s[start]] > 0:
                        num_of_chars_to_be_included += 1
                        print s[start] + ' : incrementing num_of_chars_to_be_included to: ' + str(num_of_chars_to_be_included)

                # Move start forward to find a smaller window
                print 'moving window : start'
                start += 1

            # Move end forward to find another valid window
            print 'MOVING FWD ' + s[end]
            end += 1

        if min_window_length == len(s) + 1:
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_length]
