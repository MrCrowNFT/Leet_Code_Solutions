#Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.

#Example 1:

#Input: nums = [1,1,1,2,2,3], k = 2
#Output: [1,2]
#Example 2:

#Input: nums = [1], k = 1
#Output: [1]

# We will use bucket sort solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap for counting to get frequency
        count = {}
        # array with length = len(nums) +1 because thats the max amount of times
        # a digit can repeat. the index will be the frecuency
        freq = [[] for i in range(len(nums)+1)]

        for n in nums: 
            # Counting by iterating through the array
            count[n] = 1 + count.get(n,0)
        # Now we iterate through every value we counted and get the value with .items method
        # n=number, c=count
        for n, c in count.items():
            # so in index c, we append number n, meaning that n appears c times
            freq[c].append(n)

        # We create an array for the response
        res = []
        # we iterate though this array in descending order
        # So range len of frec -1 to go from the highest index to the 0 index
        # the last -1 is so that i goes on desending order 
        for i in range(len(freq) - 1, 0, -1):
            # we get the list within that index
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res