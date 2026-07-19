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


s="5206"
st=""
prev=0

for i in s:
    if int(i)!=0 and int(i)%2!=0:
        st+=i
        if prev>int(st):
            prev=int(st)
    else:
        st=""
        prev=0
print(st)