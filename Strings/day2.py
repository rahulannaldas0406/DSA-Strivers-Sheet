'''Count Number of Substrings

Problem Statement: You are given a string s and a positive integer k.
Return the number of substrings that contain exactly k distinct characters.'''


# def brute_force(arr,k):
#     count=0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             distict=set(arr[i:j+1])

#             if len(distict)==k:
#                 count+=1
#     return count 


'''def Better_code(s,k):
    count=0
    for i in range(len(s)):
        freq={}
        for j in range(i,len(s)):
            freq[s[j]]=freq.get(s[j],0)+1

            if len(freq)==k:
                count+=1
    return count
        

a="pqpqs"
k=2
print(Better_code(a,k))'''




