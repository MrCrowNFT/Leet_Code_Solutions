## Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#### Example 1:
Input: nums = [3,2,3]
Output: 3

#### Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
#### Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

### My solution:
````python 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #I can use a hashmap, count the elements, put it
        #into an array and return the element > n/2, that will 
        #be the las element
        count = {}

        #it will have the lenght of the list, since is the max value
        # the majority element may have
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            #we use count.get, so that if the element does not exists 
            #it returns 0
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            # so in index c, we append number n, meaning that n appears c times
            freq[c].append(n)

        # we iterate though this array in descending order
        # So range len of frec -1 to go from the highest index to the 0 index
        # the last -1 is so that i goes on desending order 
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                if i > len(nums)/2:
                    return n
````

The runtime was 24 ms, Horrible!!! Try again