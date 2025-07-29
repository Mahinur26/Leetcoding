#Easy

#Brute Force Method:
#Put both Strings into a list and sort them
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(list(s)) == sorted(list(t)))

# Time Complexity: O(n log n) where n is the length of the strings due to sorting
# Space Complexity: O(n) for storing the Strings in a new sorted list


#More Efficient Method:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #If the Strings aren't the same len they can't be anagrams
        if len(s) != len(t):
            return False

        dict1 = {}
        for char in s:
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        for char in t:
            if char in dict1:
                dict1[char] -= 1
            else:
                return False
        
        for count in dict1.values():
            if count != 0:
                return False
        
        return True
        