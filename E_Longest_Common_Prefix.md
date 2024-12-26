#### Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


## Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

## Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

## Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

### My solution

````python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #we need an empty string fot the ans
        res = ""
        #Now we sort the list
        strs = sorted(strs)

        #we are going to compare the first and last string
        #since it's sorted, it should work
        first = strs[0]
        last = strs[len(strs) -1]

        #now we iterate through the strings, until the length
        #of the shortest string
        for i in range(min(len(first), len(last))):
            #if the char is not equal in both, we return the result
            # otherwise we append it
            if first[i] != last[i]:
                return res
            res += first[i]
        #if we get to the end of the strings we return res
        return res

````