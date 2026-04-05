'''
Random | Remove Duplicates in String II

You are given a string s and an integer k. Write a function to continuously remove all k adjacent duplicates from s, where the "adjacent" characters are equal, until none remain.
For instance, if k is 3 and the string is "daaabbbaa", since we have "aaa" and "bbb" as adjacent triples, the function should transform the string to "daa", removing the "aaa" substring and "bbb" substring.
Examples:


s = 'abcd'
k = 2
output: 'abcd'

s = 'deeedbbcccbdaa'
k = 3
output: 'aa'

s = 'pbbcggttciiippooaais'
k = 2
output: 'ps'

s = 'aaabbbacd'
k = 3
output: 'acd'

'''

## TO & SO: O(n)

def identify_adjacent(s: str, k: int) -> str:
    stack = [] # (ch, count)
    for i, ch in enumerate(s):
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1
            # ch, cnt = stack.pop()
            # cnt += 1
            # stack.append([ch, cnt])
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([ch, 1])

    res = ""
    for ch, cnt in stack:
        res += ch * cnt
    return res

    
# debug your code below
# print(identify_adjacent("abcd", 2))
# print(identify_adjacent("aaa", 2))
# print(identify_adjacent("deeedbbcccbdaa", 3))

### Testing Phase ###
def run_tests():
    tests = [
        # Example 1 from the book
        ("abcd", 2, "abcd"),
        # Example 2 from the book
        ("deeedbbcccbdaa", 3, "aa"),
        # Example 3 from the book
        ("pbbcggttciiippooaais", 2, "ps"),
        # Example 4 from the book
        ("aaabbbacd", 3, "acd"),
        # Additional test cases
        ("aaa", 2, "a"),
        ("aabbcc", 2, ""),
        ("abcde", 3, "abcde"),
        ("aaabbbcccddd", 3, ""),
        ("aabbccddeeffgghhii", 2, ""),
        ("xyzxyzxyz", 3, "xyzxyzxyz")
    ]
    
    for i, (s, k, expected) in enumerate(tests):
        result = identify_adjacent(s, k)
        print(f"Test case {i+1}: s='{s}', k={k}, expected='{expected}', got='{result}'")
        assert result == expected, f"Test case {i+1} failed: expected '{expected}', got '{result}'"
    print("All test cases passed!")


if __name__ == "__main__":    run_tests()