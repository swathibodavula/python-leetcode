"""Given two strings s and t, return the minimum-length substring of s such that every character in t (including duplicates) is included in that substring. If no such substring exists, return the empty string.
"""

from copy import deepcopy

def min_window(s: str, t: str) ->str:
    """I will be using a sliding window with two pointers. The window expands to the right until it contains every required character, then contracts from the left while it remains valid, recording the smallest valid window seen.
    
    The `have` counter is what keeps this fast. Instead of comparing the two dicts on every step to ask "is the window valid yet?", we just count how many characters have hit their required amount. Note the `==` in the increment — we only bump `have` at the exact moment a character's count reaches what we need, not every time it's at or above it.
    
    Time complexity: O(n+m)"""
    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    window = {}
    have, required = 0, len(need)
    best_len = float('inf')
    best_range = (0, 0)
    left = 0

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            have += 1
        
        while have == required:
            if right-left + 1 < best_len:
                best_len = right-left + 1
                best_range = (left, right)
            
            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] < need[lc]:
                have -=1
            left += 1
    l, r = best_range
    return s[l:r+1] if best_len != float('inf') else ""


if __name__ == '__main__':
    print(min_window("cabwefgewcwaefgcf", "cae"))
    print(min_window('a', "aa"))
