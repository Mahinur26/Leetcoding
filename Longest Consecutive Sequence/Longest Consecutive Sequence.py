#Medium

#My solution using .sort() function
#Less optimal
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:        
        #checks the edge case of if the array is empty
        if(len(nums) == 0):
            return 0
        #Sorts the list of numbers
        #Better than using sorted() as it uses the same nums array
        nums.sort()
        maxSeq = 1
        curMax = 1
        #Loops through everything except the first element as its already added to the max length
        for i in range(1, len(nums)):
            #Checking if the current number is the following sequence for the next
            if(nums[i-1] == (nums[i]-1)):
                curMax += 1
                if(curMax>maxSeq):
                    maxSeq = curMax
            #If the values are equal, then nothing will happen
            #If they're different, that means a new sequence so the curMax will be reset
            elif(nums[i-1] != nums[i]):
                curMax = 1
        
        return maxSeq
        return maxSeq
    #Time Complexity: O(nlogn)
    #Space Complexity: O(1)