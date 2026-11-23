class Solution:
    """Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false."""
    def checkString(self, s: str) -> bool:
        a_index = None
        b_index = None
        for i in range(len(s)):
            if s[i] == "a":
                a_index = i
            else:
                b_index = i
            
            if a_index is not None and b_index is not None:
                if a_index > b_index:
                    return False
        return True

        