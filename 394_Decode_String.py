def decodeString(s):
    stack = []
    temp = []
    for i, fc in enumerate(s):
        if fc != ']':
            stack.append(fc)
            continue
        elif fc == ']':
            temp = []
            nums = []
            for j in range(len(stack) - 1, -1, -1):
                if stack[j] != '[':
                    temp.append(stack.pop())
                else:
                    stack.pop()
                    break
            for j in range(len(stack) - 1, -1, -1):
                if stack[j].isdigit():
                    nums.append(stack.pop())
                else:
                    break
            temp.reverse()
            nums.reverse()
            print(nums)
            for c in int(''.join(nums)) * temp:
                stack.append(c)
    return ''.join(stack)


print(decodeString('3[a10[Hello]]'))
# print(decodeString('40[leetcode]'))