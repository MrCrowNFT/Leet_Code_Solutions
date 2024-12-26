#Longest Consecutive Sequence

#Given an unsorted array of integers nums, return the length of the longest 
# consecutive elements sequence.

#You must write an algorithm that runs in O(n) time.

#Example 1:
#Input: nums = [100,4,200,1,3,2]
#Output: 4
#Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

#Example 2:
#Input: nums = [0,3,7,2,5,8,4,6,0,1]
#Output: 9

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #So first we put the array into a set
        numSet = set(nums)
        #We want to keep track of the longest sequence
        longest = 0
        
        #We iterate through the nums set
        for n in nums:
            # we need to check if a num is the beggining of a sequence
            # if n is the start then, (n-1) does not exist in the set
            if (n-1) not in numSet:
                #We want to keep track of the length of the sequence
                length = 0
                # now we look for the next num in the sequence
                # (if it exists) by looking for (n+1)
                # it starts counting from n, and adding to the length as long as,
                # the next n+length exists
                while (n + length) in numSet:
                    length += 1
                #since we may potentially find the longest sequence
                # we need to update the longest
                # it must chose the greater value between the previous
                # longest and the length it just counted
                longest = max(length, longest)
        return longest
        
