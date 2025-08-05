class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        no_removed = 0
        max_len = 0

        for i in range(len(s)):

            while (s[i] in charSet):
                charSet.remove(s[no_removed])
                no_removed += 1

            charSet.add(s[i])
            max_len = max(max_len, i - no_removed + 1)

        return max_len




solution = Solution()
s = "abcabcbb"
# s = "bbbbb"
print(solution.lengthOfLongestSubstring(s=s))