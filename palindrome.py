#For String
def is_palindrome(s):
    return s == s[::-1]  


word = "madam"
print(is_palindrome(word))


#For Number
def is_palindrome_number(n):
    return str(n) == str(n)[::-1]  


num = 121
print(is_palindrome_number(num))  
