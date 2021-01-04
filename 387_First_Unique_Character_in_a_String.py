# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.


# Note: You may assume the string contains only lowercase English letters.


class Solution:
    def firstUniqChar(self, s):
        # create distionary with counts(in 3.7 it has the same order)
        counts = dict()
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for idx, char in enumerate(s):
            if counts[char] == 1:
                return idx

        return -1
