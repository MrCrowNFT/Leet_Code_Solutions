""""
 Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #we use a stack, appending the numbers as they appear, when an opertion comes, 
        #we get the numbers from the stack, pop them, and replace them with the solution
        #to the equation of using said numbers with the given operation, so and so until
        #only one number remains. if solution is negative, it rounds up to 0
        
        stack=[]
        for c in tokens:
            if c == "+":
                #append the sum of poping the las two values
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                #when substracting we want the following
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                #when dividing we want the following, now we cast into an int
                #since ints are only positive it will automatically round it up to zero
                stack.append(int(b/a))

            #else is number, we have to cast it as number since its a character
            else:
                stack.append(int(c))
        return stack[0]

    """
    time complexity = O(n)

    """
        