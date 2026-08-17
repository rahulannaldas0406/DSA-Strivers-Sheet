'''Count Number of Substrings

Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.'''

def count_substr(s,k):
    a=set()
    sub_str=""
    count_substr+=1
    valid_arr=[]
    right=1
    for left in range(len(s)):
        sub_str+=s[left]
        


    



s="pqpqs"
k=2
print(count_substr(s,k))
