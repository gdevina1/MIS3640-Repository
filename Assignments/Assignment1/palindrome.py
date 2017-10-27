def isPalindrome(s):
    '''
    Question: Write a recursive function isPalindrome(string) that returns True if string is a palindrome, that is, 
    a word that is the same when reversed. Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
    Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.
    '''
    '''
    Function isPalindrome takes a string s and checks to see if it is a palindrome by using recurssion to
    check if pairs of first and last letters of the string contain the same character. If the first pair of letters are of the
    same character, the function continues its recurssion until it either has less than 2 characters left returning True, or if it finds
    a pairs that does not contain matching characters, where the function returns False, for string s is not a palindrome.
    '''

    if len(s) < 2:               #stops recurssion if there is less than 2 characters left in string s
        return True
    elif s[0] != s[-1]:          #stops recurssion if first and last characters are not the same
        return False
    return isPalindrome(s[1:-1]) #checks if the pairs of first and last letters are palindrome


inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    print("That's a palindrome.")
else:
    print("That isn't a palindrome.")

