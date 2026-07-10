"""Given an unsorted array of integers, return the length of the longest consecutive elements sequence. Your algorithm must run in O(n) time.

Input: [100, 4, 200, 1, 3, 2]
Output: 4  — sequence: [1, 2, 3, 4]

Input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
Output: 9  — sequence: [0,1,2,3,4,5,6,7,8]

Input: [] → Output: 0 """

def longest_consecutive(nums):
    """Time: O(n) - each number is visited at most twice: once by the outer loop and at most once by a while loop (only sequence starts spawn a while loop, so all iterations combined <= n).
    Space: O(n) - the set stores all unique numbers."""
    num_set = set(nums)
    best = 0

    for i in num_set:
        if i-1 not in num_set:
            length = 1
            while i+length in num_set:
                length+=1
        best = max(best, length)
    return best

        

if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(longest_consecutive([]))