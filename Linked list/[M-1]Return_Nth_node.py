"""
Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
 

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #we will be using a dummy node
        dummy = ListNode(0, head)
        #we will use two pointer
        left, right = dummy, head

        #here we use the two pointers to find the n node
        while n>0 and right:
            right = right.next
            n-=1
        while right:
            left = left.next
            right = right.next
        #here we delete the node by assigning the next as the next of the next
        left.next = left.next.next
        return dummy.next
        """
        time = O(n)
        """
    #*Need to check this again, didn't quiet get the explenation 