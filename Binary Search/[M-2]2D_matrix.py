"""
Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #This is like binary search square, we use it to finde the row
        #once in the row we use another to find the target
        ROWS, COLS= len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        while top <= bot: 
            row = (top+ bot) //2 
            #if target is greater than right most value(that's what the -1 means)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break

        #Check if it is valied, since it could have broken in the break before 
        # reaching the while check
        if not (top<=bot):
            return False
        #now we know the row
        row = (top + bot) //2
        l, r = 0, COLS -1
        while l <= r:
            midpoint = (l+r)//2
            #compare to the value in the matrix
            if target == matrix[row][midpoint]:
                return True
            elif target > matrix[row][midpoint]:
                l = midpoint +1
            else:
                r = midpoint - 1
        return False
            
