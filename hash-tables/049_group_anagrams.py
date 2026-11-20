"""Given a list of strings, group all anagrams together and return a list of groups. Each group should contain all strings that are anagrams of each other. The order of groups and order within each group does not matter.

Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

Input: [""]
Output: [[""]]

Input: ["a"]
Output: [["a"]]"""

def group_anagrams(strs):
    """ Given a list of strings, group all anagrams together...
    Time: O(n * k log k) - n strings, sorting each of length k
    Space: O(n*k)"""

    output = {}
    anagrams = []
    for i in strs:
        sorted_text = "".join(sorted(i))
        if sorted_text not in output.keys():
            output[sorted_text] = []
        output[sorted_text].append(i)
    for i in output:
        anagrams.append(output[i])
    
    return(anagrams)

def group_anagrams2(strs):
    """ Given a list of strings, group all anagrams together...
    Time: O(n * k) - n strings, maximum of length k characters    
    Space: O(n*k)"""

    anagrams = {}
    for word in strs:
       counts = [0]*26

       for letter in word:
           counts[ord(letter) - ord('a')] += 1

       key = tuple(counts)
       if key not in anagrams:
           anagrams[key] = []
       anagrams[key].append(word)

    return list(anagrams.values())

if __name__ == "__main__":
    print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams([""]))

    print(group_anagrams2(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams2([""]))

