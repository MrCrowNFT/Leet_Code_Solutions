"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #we need two counters, one for open and one for close parenthesis
        #we know two things. first, that the counters should never be greater than n
        #and second, that we can only add to the add to the closing parenthesis 
        #if close < open. it will only be valid if open == close == n
        #this require a backtracking solution: recursevly and a stack
        stack = []
        res = []
        #we'll nest a function
        def backtrack(openN, closedN):
            if openN == closedN == n:
                #we take every character in the stack and join them together 
                #into a empty string. Then append it to the result
                res.append("".join(stack))
                return 
            if openN < n:
                #adding a openparenthesis and updating the counter 
                #and backtracking with the new counter
                stack.append("(")
                backtrack(openN +1, closedN)
                #after backtracking we pop it from the stack
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN +1)
                stack.pop()
        #we call the function
        backtrack(0,0)
        return res

        """
        Don't really understand exactly why this works
        """