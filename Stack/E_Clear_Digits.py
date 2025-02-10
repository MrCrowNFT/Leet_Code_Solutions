"""
3174. Clear Digits

You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
"""
#My solution
class Solution:
    def clearDigits(self, s: str) -> str:
        #first we need a stack
        stack = []
        res = ""

        #then we iterate through the string, if is alpha we add it to the stack
        #else (meaning is a number), we pop the last added item (closest non-digit 
        #character to its left.)
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                stack.pop()

        #now we put all the remaining items of the stack into the res string and return it
        for item in stack:
            res += item

        return res
        