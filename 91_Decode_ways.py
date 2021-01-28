def numDecodings(s):
    d = []
    d.append(1)
    d.append(1)
    if len(s) == 1 and s[0] == "0": return 0
    for i in range(2, len(s) + 1):
        td, od = 0, 0
        if 10 <= int(s[i - 2: i]) <= 26:
            td = 1
        if s[i - 1] != "0":
            od = 1
        d.append(td*d[i -2] + od*d[i - 1])
    return d[-1]

print(numDecodings('12'))
print(numDecodings('0'))
print(numDecodings('123'))
print(numDecodings('226'))
print(numDecodings('1'))