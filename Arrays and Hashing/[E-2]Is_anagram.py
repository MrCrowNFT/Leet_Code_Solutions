# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If strings length is different we immediately return false
        if len(s) != len(t):
            return False

        # We make two dictionaries, the idea is to iterate through the strings
        # every letter we add it to the hashmap and add +1 to ITS counter
        # the we check if both dictionaries have the same letter with the same counters
        countS, countT = {},{}

        for i in range(len(s)):
            # The get keyword will get the value and if the letter does not exists in the 
            # hashmap it will 0 (if we don't use get, if the letter is not on the map
            # the execution will fail)
            countS[s[i]] = 1 +  countS.get(s[i], 0)
            countT[t[i]] = 1 +  countT.get(t[i], 0)

        # Now we iterate though the hash maps and compare the counts
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    
    # Other way of solving this without using memory would be by sorting the 
    # strings and comparing them

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
            