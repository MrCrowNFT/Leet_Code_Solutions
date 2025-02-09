#Two Sum II - Input Array Is Sorted

#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. Let these two numbers 
# be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, added by one as an integer array 
# [index1, index2] of length 2.

#The tests are generated such that there is exactly one solution. You may not use the same 
# element twice.

#Your solution must use only constant extra space.

 
#Example 1:
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

#Example 2:
#Input: numbers = [2,3,4], target = 6
#Output: [1,3]
#Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

#Example 3:
#Input: numbers = [-1,0], target = -1
#Output: [1,2]
#Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

#Constraints:
#2 <= numbers.length <= 3 * 104
#-1000 <= numbers[i] <= 1000
#numbers is sorted in non-decreasing order.
#-1000 <= target <= 1000
#The tests are generated such that there is exactly one solution.


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #We can use the fact that the array i sorted to our adventage
        #We can use a pointer at the beggining(left) and one at the end(right)
        #So we can shift the pointer inwards, one at a time until we find the pair
        #so if the sum is too big we move the right pointer to the left to 
        #lower the sum
        #if the sum is too small we move the left pointer to the right 
        #to increase the sum
        #since we are guranted a solution, eventually we'll get there
        l, r = 0, len(numbers) -1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                #they have to be added 1 because "added by one" in the description
                return [l +1 , r + 1]