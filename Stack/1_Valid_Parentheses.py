'''
Question: Given a string that contains just '(', '{', '[', ')', '}', ']'
Determine if the input is valid

Considered valid if...
Open brackets must be closed by same type of bracket
    ( closes ), { closes }, and [ closes ]

Open brackets must be closed in order
    ([)] is invalid, has to be ([])

Every closed bracket has a corresponding open bracket of same type
    At end of string it can't have anything in string
'''

'''
Idea: Use a stack to save the open brackets and when a closed bracket occurs, we check if it matches

Edge cases:
1. First character of string is a closing bracket
2. Popping from the stack if there's nothing in it
'''

def isValid(s:str):
    # Check for edge case 1
    if s[0] == ']' or s[0] == ')' or s[0] == '}':
        return False
    # Create a stack
    stack = []
    for bracket in s:
        # Check if bracket is open
        if bracket == '(' or bracket == '{' or bracket == '[':
            stack.append(bracket)
        #If it's not, we assume it's closed
        else:
            # Edge case 2
            if len(stack) == 0:
                return False
            # Pop stack into variable
            popped = stack.pop()
            #Check if the proper close is connected to opening
            if (bracket == ')' and popped == '(') or (bracket == ']' and popped == '[') or (bracket == '}' and popped == '{'):
                continue
            else: return False
    # If there's still something in the stack after, we return false because it's not completed
    if len(stack) > 0:
        return False
    # IF EVERYTHING IS GOOD, RETURN TRUE
    return True

print(isValid('(]'))