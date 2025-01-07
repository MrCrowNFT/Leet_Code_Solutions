"""
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        #We will use a stack
        stack=[]
        #we are gonna map closing parenthesis to open parenthesis of each type
        #the keys are the closing parenthesis
        closeToOpen = { ")":"(",
                        "]":"[", 
                        "}":"{"}
        for c in s:
            #since it the closng parenthesis are the keys, we can check them
            if c in closeToOpen:
                #we check if the las item in the stack is the matching parenthesis to the closing one
                if stack and stack[-1] == closeToOpen[c]:
                    #pop last item
                    stack.pop()
                else: 
                    return False
            #if is not a closing bracket we add it to the stack
            else:
                stack.append(c)
        #If the stack is empty, every opening parenthesis mathed each and pop and thus return true
        return True if not stack else False


        