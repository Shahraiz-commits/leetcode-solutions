class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            # If duplicate, shrink window from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Expand window
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

