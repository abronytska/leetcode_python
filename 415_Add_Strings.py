def addStrings(num1, num2):
    res = list()
    n_next = 0
    len1 = len(num1) - 1
    len2 = len(num2) - 1

    while len1 >= 0 or len2 >= 0:
        n1 = ord(num1[len1]) - ord('0') if len1 >= 0 else 0
        n2 = ord(num2[len2]) - ord('0') if len2 >= 0 else 0
        n = n1 + n2 + n_next

        if n >= 10:
            res.append(n % 10)
            n_next = (n - n % 10) / 10
        else:
            res.append(n)
            n_next = 0

        len1 -= 1
        len2 -= 1

    if n_next != 0:
        res.append(n_next)
    res.reverse()
    res = [str(i).replace('.0', '') for i in res]

    return ''.join(res)



print(addStrings('398', '1256'))