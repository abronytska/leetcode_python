def minRemoveToMakeValid(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            elif stack and s[stack[-1]] == ')':
                stack.append(i)
            elif not stack:
                stack.append(i)
    stack.reverse()
    for el in stack:
        s = s[:el] + s[el + 1:]
    return s


print(minRemoveToMakeValid('lee(t(c)o)de)'))
print(minRemoveToMakeValid('a)b(c)d'))
print(minRemoveToMakeValid('))(('))
print(minRemoveToMakeValid('(a(b(c)d)'))