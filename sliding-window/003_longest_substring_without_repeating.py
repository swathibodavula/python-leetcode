"""Given a string s, return the length of the longest substring that contains no repeated characters. A substring must be contiguous — no skipping characters.

s = "abcabcbb"  ->  3    (longest is "abc")
s = "bbbbb"     ->  1    (longest is "b")
s = "pwwkew"    ->  3    (longest is "wke")
s = ""          ->  0 """

def length_of_longest_substring(s: str) -> int:
    """Time: O(n) — right visits each character once (n steps), and   left only ever moves forward, so all while-loop removals combined ≤ n.
       Two shared budgets of n → O(n) + O(n) = O(n).
       Space: O(min(n, m)) — the set holds the current window's characters,
       which can't exceed the number of distinct characters m
       (e.g., 26 for lowercase letters) or the string length n."""
    best = 0
    left = 0
    right = 0
    substring = set()

    for right in range(len(s)):
        if s[right] in substring:
           while s[right] in substring:
               substring.remove(s[left])
               left+=1  
        substring.add(s[right])

        best = max(best, right-left+1)
    return best

if __name__ == "__main__":
    print(length_of_longest_substring("pwwkew"))
    print(length_of_longest_substring("tmmzuxt"))
    print(length_of_longest_substring("abcbe"))
    print(length_of_longest_substring("dvdf"))
    print(length_of_longest_substring("abba"))
    print(length_of_longest_substring("aab"))
    print(length_of_longest_substring("abcdef"))
    print(length_of_longest_substring("aaaa"))
    print(length_of_longest_substring("a"))
    print(length_of_longest_substring(""))

