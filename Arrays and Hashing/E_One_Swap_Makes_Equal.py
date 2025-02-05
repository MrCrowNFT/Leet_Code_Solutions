"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation 
where you choose two indices in a string (not necessarily different) and swap the 
characters at these indices.
Return true if it is possible to make both strings equal by performing at most one 
string swap on exactly one of the strings. Otherwise, return false.

 
Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
#My solution: class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        #we create a list
        diff = []

        #we iterate through the strings and store the pairs that are not equal
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                diff.append((s1[i], s2[i]))
            #if greater than two we exit early
            if len(diff) > 2:
                return False

        #if no diff means its equal, therefor true
        if len(diff) == 0: 
            return True
        #if dif is exactly two we still need to compare if the swapping makes them equal
        #so we compare the first char on the first pair with the second char of the second pair
        if len(diff) == 2 and diff[0] == diff[1][::-1]:
            return True
        return False