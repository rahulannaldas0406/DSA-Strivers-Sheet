#Remove Outermost Parentheses

'''Example 1:
Input:
 s = "((()))"
Output:
 "(())"
Explanation:
 The input string is a single primitive: "((()))".  
Removing the outermost layer yields: "(())"'''


'''def removeOuterParentheses(s) :
        res=""
        level=0
        for char in s:
            if char=='(':
                if level>0:
                    res+=char
                level+=1

            elif char==')':
                level-=1

                if level>0:
                    res+=char
                
        return res
s = "(()())(())"
print(removeOuterParentheses(s))'''


'''Reverse Words in a String


15

Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ).
 A word is defined as a sequence of non-space characters.
 The words in s are separated by at least one space. Return a string with the words in reverse order, concatenated by a single space.'''

#Solution 

'''def rev_word(st):
    arr=st.split()

    arr.reverse()
    return " ".join(arr)
st="My name is rahul"
print(rev_word(st))'''

'''Largest Odd Number in a String.


10

Problem Statement: Given a string s, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string s.
The number returned should not have leading zero's. But the given input string may have leading zero.'''

#Solution

'''def largestOddNumber(num):
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""

num="52"
print(largestOddNumber(num))'''


'''Longest Common Prefix


9

Problem Statement: Write a function to find the longest common prefix string amongst an array of strings. 
If there is no common prefix, return an empty string "".'''

#Solution

#Optimize

'''def largestCommonPrefix(strs):
    if not strs:
        return ""
    
    strs.sort()

    first=strs[0]
    last=strs[-1]

    i=0

    while i<len(first) and i<len(last):
        if first[i]!=last[i]:
            break
        i+=1

    return first[:i]

strs=["flower", "flow", "flight"]
print(largestCommonPrefix(strs))'''


'''Isomorphic String


11


Problem Statement: Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Examples'''

'''def isomorphic(s,t):
    m1,m2=[0]*256 ,[0]*256

    n=len(s)

    for i in range(n):
        if m1[ord(s[i])]!=m2[ord(t[i])]:
            return False
        
        m1[ord(s[i])]=i+1
        m2[ord(t[i])]=i+1

    return True

s="foo"
t="bar"

print(isomorphic(s,t))'''

#Check if one string is rotation of another

'''Problem Statement: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.'''

#This is the optimize code O(n) so 

#Interview explain 

'''Imagine the string is arranged in a circle.

Every rotation simply changes the starting point while preserving the order.

Concatenating the string with itself contains every possible starting point exactly once, so every valid rotation appears as a substring of s + s.'''

#I Saw this trick in  leetcode 

#If they could ask is there any other approach to solve without s+s 

''' Yes,Rotate the string one position at a time.
Compare it with goal ''' # Time complexity is O(n^2)


'''def rotate(s,goal):
    value=s+s

    if len(s) != len(goal):
        return False

    if goal in value:
        return True
    else:
        return False

s="abc"
goal="ab"
print(rotate(s,goal))'''


#Check if two Strings are anagrams of each other

'''Problem Statement: Given two strings, check if two strings are anagrams of each other or not.'''


'''def isAnagram(s, t):

    if len(s) != len(t):
        return False

    count = {}

    for ch in s:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    for ch in t:
        if ch in count:
            count[ch] -= 1
        else:
            return False

    for value in count.values():
        if value != 0:
            return False

    return True


print(isAnagram("listen", "silent"))'''

'''s="tree"

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

ans = sorted(freq.items(), key=lambda x: (-x[1], x[0]))'''


#Maximum Nesting Depth of Parenthesis

'''Problem Statement: Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses'''

def nested(s):
    max_count=0
    count=0
    for i in s:
        if i=="(":
            count+=1
        elif i==")":
            
            count-=1
        max_count=max(max_count,count)
    return max_count


s ="(1)+((2))+((((3))))"
print(nested(s))
