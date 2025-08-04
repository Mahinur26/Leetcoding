#Medium

#My solution/Very suboptimal solution:

#I used a dictionary to contain the frequency of each number, then I used a while loop to find the maximum frequency k times
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #Number:Frequency
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        val = k
        l1 = []
        while k > 0:
            key = max(dictionary, key=dictionary.get)
            l1.append(key)
            del dictionary[key]
            k -= 1
        return l1
#Time Complexity: O(n * k) where n is the number of elements in nums and k is the number of unique elements
#Space Complexity: O(n) where n is the number of unique elements in nums