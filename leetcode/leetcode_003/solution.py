class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        longest, start, visited = 0, 0, [False for _ in range(256)]
        for ind, val in enumerate(s):
            if not visited[ord(val)]:
                visited[ord(val)] = True
            else:
                while val != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            longest = max(longest, ind - start + 1)
        return longest