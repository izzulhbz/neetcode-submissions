class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in seen_s:
                seen_s[ch] += 1
            else:
                seen_s[ch] = 1
        
        for ch in t:
            if ch in seen_t:
                seen_t[ch] += 1
            else:
                seen_t[ch] = 1
        
        if seen_s == seen_t:
            return True
        return False