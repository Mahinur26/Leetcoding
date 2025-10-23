#Easy

#Brute Force Method:
#Can sort both strings and compare them, if they are the same then they are anagrams
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time Complexity: O(n log n) where n is the length of the strings due to sorting
# Space Complexity: O(n) for storing the Strings in a new sorted list


#More Efficient Method:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Edge case: If the Strings aren't the same len they can't be anagrams
        if len(s) != len(t):
            return False

        dict1 = {}
        for char in s:
            if char in dict1:
                #If the char is already in the dictionary, add one for this char
                dict1[char] += 1
            else:
                #Otherwise create a new key-value pair with 1 as the value for that char
                dict1[char] = 1
        #Loops through each char in t and subtracts it from the dictionary
        for char in t:
            if char in dict1:
                dict1[char] -= 1
            else:
            #Edge case: If the char isn't in the dictionary, they aren't anagrams
                return False
                
        #Loops through all of the values in the dictionary to ensure they're 0
        for count in dict1.values():
            if count != 0:
                return False
        
        return True
    
#Time complexity: O(n + k) where n is the length of the strings, and k is the number of unique characters in the input.
#Space complexity: O(s) where s is the number of unique chars in String s. Also, only one dictionary is created to store the characters and their counts


#Can also be done with the collections.Counter class
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #The Counter DS counts the number of each unique occurrence in a dictionary, in this case the chars are counted 
        return Counter(s) == Counter(t)