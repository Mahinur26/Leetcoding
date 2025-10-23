#Easy
#Use the hashmap/hashset DS to determine if there are duplicate because hashmaps can’t have duplicate values.
#Can be done in Python with the set() function and comparing len(original) to len(set(original)) 
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return (len(set(nums)) != len(nums))  
    
# Time Complexity: O(n) where n is the number of elements in the input list.
# Space Complexity: O(n) for storing the unique elements in a set.