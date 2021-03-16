#longestSubString.py

def longest_sub_string(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return s
    long_string = ''
    start = 0
    for i in range(len(s)):
        if (i != len(s)-1) and s[i] == s[i+1]:
            end = i
            long_string = max(long_string, s[start:end+1])
            start = i + 1
    return long_string

def lengthOfLongestSubstring(s):
        longest_string = left = 0
        seen = {}
        
        for i, char in enumerate(s):
            if left <= seen.get(char, -1):
                left = seen[char] + 1
                print('left:{} with value {}'.format(left, s[left]))
            else:
                longest_string = max(longest_string, i + 1 - left)               
            
            seen[char] = i
            print(seen)
        return longest_string

def LongestSubstring(s):
        longest_string = start = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                start = seen[s[i]] + 1
            else:
                longest_string = max(longest_string, i - start + 1)
            seen[s[i]] = i
            # print(seen)
        return longest_string
        
def longestPalindrome(s):
    res = ""
    for i in range(len(s)):
        odd = palindrome(s, i, i)
        even = palindrome(s,i, i+1)
        res = max(odd, even, res,key=len)
    return res

def palindrome(s,l,r):
    while l>=0 and r< len(s) and s[l]==s[r]:
        l -= 1
        r += 1
    return s[l+1:r]
def main():
    # s = "abcabcbb"
    # print(longest_sub_string(s))
    # print(LongestSubstring(s))
    s = "abbd"
    print(longestPalindrome(s))
main()