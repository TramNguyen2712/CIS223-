def palindrome(S):
    if len(S) == 0: # if index is 1 then S is a palindrome
        return True
    else:
        if S[len(S) - 1] == S[0]: #if the character at the begin and the character at the end are same to each other, run the recursion
            return palindrome(S[1:len(S) - 1]) #recur on rest
        return False # return False if characters are different and the recursion will stop

print(palindrome('aibohphobia'))
#Each call is O(1) and there are n/2 function calls at O(1)
#Running time is O(n/2) that is also O(n)
