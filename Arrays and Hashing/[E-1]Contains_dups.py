# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Creating a hash set
        hashset = set()

        # Iterating through the hash set to check for dups, if no dups it will add n into the
        # set, if already exists i will return true
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
