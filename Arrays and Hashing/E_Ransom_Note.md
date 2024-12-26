## Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

#### Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

#### Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

#### Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

#### Constraints:
- 1 <= ransomNote.length, magazine.length <= 105
- ransomNote and magazine consist of lowercase English letters.

### My solution
````python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #Create two dictionaries to keep track of the count of each letter
        countR, countM = {}, {}

        #Now we iterate through the strings to get the count of each string
        for i in range(len(magazine)):
            countM[magazine[i]] = 1 + countM.get(magazine[i], 0)

        for i in range(len(ransomNote)):
            # The get keyword will get the value and if the letter does not exists in the 
            # hashmap it will 0
            countR[ransomNote[i]] = 1 + countR.get(ransomNote[i], 0)

        #Now we iterate through the counts and see if there are enough
        for c in countR:
            if countR[c] > countM.get(c, 0):
                return False
        #The return True must be outside the loop so that it only returns
        # after iterating through all the keys in countR     
        return True

####My solution took 31ms and 17MB of memory. That's awful. Try Again on another date.
````