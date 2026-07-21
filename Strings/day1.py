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