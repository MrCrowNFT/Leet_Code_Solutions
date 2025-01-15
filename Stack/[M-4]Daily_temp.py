"""
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #This problem require a monotonic decresing stack algorith (stack always in decresing order)
        res = [0] * len(temperatures)
        stack = [] #we'll be adding two values to the stack: temp, index

        for i, t in enumerate(temperatures):
            #while stack is not empty and temperature is greater than the last temp 
            #in the stack we can pop from the stack
            while stack and t > stack [-1][0]:
                #by poping we get the temp and the index
                stackT, stackInd = stack.pop()
                #and the distance it took to get a greater temp was the index - the poped indx
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        #since we already initialized the stack to be zero, we don't need to fill the zeros
        return res

"""
time = O(n)
"""