def isPalindrome(x):
    x = str(x)
    a = (x[::-1])
    print(x,a)
    if (x == a):
        return True
    else:
        return False

print(isPalindrome(123))

