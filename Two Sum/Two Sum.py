#Easy

#Brute Force Method:
#Double for loop and check which pair of indices adds up to the target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if ((nums[i] + nums[j]) == target):
                    return [i, j]

# Time Complexity: O(n^2) where n is the length of the nums list due to the nested loops
# Space Complexity: O(1) since no additional data structures are used

#Optimal Method:
#Use a dictionary to store the difference between the target and each number
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Will store as value: index
        prevVals = {}
        for index, val in enumerate(nums):
            #If the difference between the target and the current value is a key in the dictionary, return the indices
            if (target-val) in prevVals:
                return [prevVals[target-val], index]
            prevVals[val] = index

# Time Complexity: O(n) due to the single for loop iterating through the nums list
# Space Complexity: O(n) - more specifically will store up to the element right before you find the solution
#Hashmaps/dictionaries have a near O(1) lookup time so the trade for space is worth it