"""
 Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        #The dificult part is basically the fact that by definition, getting the min value
        #from a stack would mean we have to get all the items from it first and check each
        #so, by making a second stack, where we'l only add the number is lower than 
        #the last item in the stack, otherwise, add the same last num 
        #we can get the min value by just getting the last num added to it
        self.minStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        #So we get the min value between the val and the last num in stack
        #we have to take into consideration the fact that the stack may be empty
        val = min(val, self.minStack[-1] if self.minStack else val)    
        self.minStack.append(val)    

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

#this function will be returning from the minStack
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()