## Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

#### Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

#### Example 2:
Input: arr = [1,2]
Output: false

#### Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

### My Solution 
````python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #counter is an array that has the key as the number 
        #and the value as the frequency
        counter = Counter(arr)
        #Create a set for the answer
        sol = set()

        #now we iterate through the values in counter
        for v in counter.values():
            #if the value is already in the set we return false,
            #since we already found that frequency, otherwise we append
            if v in sol:
                return False
            sol.add(v)
        return True
````