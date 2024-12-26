#Valid Palindrome

#A phrase is a palindrome if, after converting all uppercase letters into 
# lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

#Given a string s, return true if it is a palindrome, or false otherwise.

#Example 1:
#Input: s = "A man, a plan, a canal: Panama"
#Output: true
#Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first we need to remove all the non alphanumeric chars
        newStr = ""

        for c in s:
            #now we check if it's alphanum
            if c.isalnum():
                #if alphanum we add it to the newStr as lower case
                newStr += c.lower()
        #We compare the newStr with the reverse newStr
        return newStr == newStr[::-1]


#There is a better solution that does not uses memory with two point solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #So we got two pointers that will start at a diferent end of the phrase  
        l, r = 0, len(s) - 1

        #the pointer to the left will be advancing right, and the one on
        # the right will advance to the left, once they pass each other
        # the while loop will end
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    #We use ASCII values to judge if alphanumeric
    def alphaNum(self, c):
        #the ord function returns the ascii value
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))