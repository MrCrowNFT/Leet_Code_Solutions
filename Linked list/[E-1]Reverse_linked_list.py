"""
Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
#There are two solutions to this problem: 

#Solution1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #there are two ways to solve this, first one is by using two pointers
        #one will point to the previus address and the other to the current address
        #and then reversing them until current is not null
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

        """
        time complexity= O(n)
        Memory complexity = O(1), since we are just using pointers
        """

#Solution 2
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #recursion
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead

        """
        Time = O(n)
        Memory= O(n)
        """
        
        
