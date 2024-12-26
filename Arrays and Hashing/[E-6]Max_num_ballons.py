"""
Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the 
word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances 
that can be formed.

 

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #i should get the count of each letter to form the word ballon
        #that are in the text
        counter = defaultdict(int)
        balloon = "balloon"

        for c in text:
            if c in balloon:
                counter[c] += 1
        if any(c not in counter for c in balloon):
            #so if we are missing a letter of balloon, means we can
            #not form it, so return 0
            return 0
        else:
            #we return the min amount of instances, have in consideration
            #that l and o repeat twice in balloon
            return min(counter["b"], counter["a"], counter["l"]//2, counter["o"]//2,counter["n"],)
        