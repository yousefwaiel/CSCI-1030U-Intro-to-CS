def palindrome_rec(str):
    if len(str) < 2:
        return True
    if str[0] != str[len(str)-1]:
        return False
    return palindrome_rec(str[1:len(str)-1])

print(palindrome_rec("leeld"))