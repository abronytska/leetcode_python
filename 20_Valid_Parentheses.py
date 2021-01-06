# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


def isValid(s):
    valid_pairs = {'(': ')', '{': '}', '[': ']'}

    stack = []

    for char in s:

        if char in valid_pairs.keys():
            stack.append(char)

        if char in valid_pairs.values():
            top_element = stack.pop() if stack else '#'

            if char != valid_pairs.get(top_element, 0):
                return False

    return not stack
    # return not stack




print(isValid('))'))  # false
print(isValid('()[]{}'))  # true
print(isValid('()}'))  # false
print(isValid('()'))  # true



