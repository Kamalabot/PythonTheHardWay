problemStatement = """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""
link = "https://leetcode.com/problems/valid-parentheses/description/"
solution = "solving"


# using the brute force logic checking failed. 
def wrongValid(chars):
    # if char @ 0 is }/ ] / ) return False
    if chars[0] == ')' or chars == '}' or chars[0] == ']':
        return False
    # create three * 2 stores for each type of brackets
    openP = 0
    closeP = 0
    openF = 0
    closeF = 0
    openS = 0
    closeS = 0
    print(openP, closeP, openF, closeF, openS, closeS)
    for ind, char in enumerate(chars):
        # check if char is (
        if char == '(':
            openP += 1
        # check if char is [
        elif char == '[':
            openS += 1
        # check if char is {
        elif char == '{':
            openF += 1
        # check if char is )
        if char == ')':
            # if there is no ( before this
            if openP == 0:
                return False
            # check if there are other unpaired brackets
            if openF != closeF:
                # check if there are } in rest of string
                if '}' not in chars[ind:]:
                    return False
            if openS != closeS:
                # check if there are ] in rest of string
                if ']' not in chars[ind:]:
                    return False
            closeP += 1
        # check if char is ]
        elif char == ']':
            # if there is no [ before this
            if openS == 0:
                return False
            # check if there are other unpaired brackets
            if openF != closeF:
                # check if there are } in rest of string
                if '}' not in chars[ind:]:
                    return False
            if openP != closeP:
                # check if there are ] in rest of string
                if ')' not in chars[ind:]:
                    return False

            closeS += 1
        # check if char is }
        elif char == '}':
            # if there is no { before this
            if openF == 0:
                return False
            # check if there are other unpaired brackets
            if openS != closeS:
                # check if there are } in rest of string
                if ']' not in chars[ind:]:
                    return False
            if openP != closeP:
                # check if there are ] in rest of string
                if ')' not in chars[ind:]:
                    return False
            closeF += 1
    # if the number of open and closed brackets are equal then return True
    print(openP, closeP, openF, closeF, openS, closeS)
    if openP == closeP and openS == closeS and openF == closeF:
        return True
    else:
        return False


Approach = """
Here is the step-by-step approach of the algorithm:

Initialize an empty stack.

Traverse the input string character by character.

If the current character is an opening bracket (i.e., '(', '{', '['),
push it onto the stack.

If the current character is a closing bracket (i.e., ')', '}', ']'),
check if the stack is empty.
If it is empty, return false, because the closing bracket does not have a
corresponding opening bracket.
Otherwise, pop the top element from the stack and check if it matches
the current closing bracket. If it does not match, return false,
because the brackets are not valid.

After traversing the entire input string, if the stack is empty, return true,
because all opening brackets have been matched with their corresponding
closing brackets. 
Otherwise, return false, because some opening brackets have not been matched
with their corresponding closing brackets.
"""


def isValid(chars):
    stack = []  # intialize the stack
    # traverse the input string char by char
    for char in chars:
        # check if char is (,{, [
        if char in '{[(':
            # push into the stack, at the top
            stack.insert(0, char)
        if char == ")":
            if len(stack) == 0:
                return False
            else:
                # pop the top item in stack
                k = stack.pop(0)
                # check if k is pair of char
                if k != "(":
                    # return False, as brackets no match
                    return False
        elif char == "}":
            if len(stack) == 0:
                return False
            else:
                # pop the top item in stack
                k = stack.pop(0)
                # check if k is pair of char
                if k != "{":
                    # return False, as brackets no match
                    return False
        elif char == "]":
            if len(stack) == 0:
                return False
            else:
                # pop the top item in stack
                k = stack.pop(0)
                # check if k is pair of char
                if k != "[":
                    # return False, as brackets no match
                    return False

    if len(stack) != 0:  # if there is pending elems in stack
        return False  # return False
    else:
        return True  # else return True 


assert isValid("()") is True
assert isValid("(){}[]") is True
assert isValid("(]") is False

# print(isValid("([)]"))
assert isValid("([)]") is False
assert isValid("{[]}") is True
