# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We need to map the count of chars to list of anagrams
        hashmap = defaultdict(list)
        
        for s in strs:
            # We will count how many of each letter in the alphabet it has
            # That why 26, and every counter begins at 0
            count = [0] * 26
            for c in s:
                # So in order to get eache letter in the string we use its askii value
                # we substract a so that we get a value between 0-26
                count[ord(c)-ord("a")] += 1
            # So we are adding it to the hashmap. Word count -> string
            hashmap[tuple(count)].append(s)
        # Now we return only the values
        return list(hashmap.values())