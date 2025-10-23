#Medium

#My solution/Less optimal solution:
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapOfAnagrams = {} #sortedWord tuple: Word str
        for word in strs:
            #Lists aren't hashable, but tuples are as they are immutable - keys must be immutable
            #The sorted() function sorts the chars in a list like ['a', 'c', 'e']
            key = tuple(sorted(word))
            if key in mapOfAnagrams:
                mapOfAnagrams[key].append(word)
            else:
                #If the key doesn't exist, the first index for the value/list will be the word
                mapOfAnagrams[key] = [word]
        #Returns the list of values in a list as asked [[], [], []]
        return list(mapOfAnagrams.values())

#Time Complexity: O(n log n) 
#Space Complexity: O(n) 

#Optimal solution:
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagramsDict = defaultdict(list)
        for word in strs:
            #Creates an array for word and its chars with 26 0's to represent each letter in the alphabet
            count = [0] * 26
            for char in word:
                #Subtracting the ASCII values (with ord() function) from lowercase a-z
                #These values are contiguous so the subtraction will output an index from 0-25 inclusive
                #Adding 1 to the index for the corressponding character
                count[ord(char) - ord('a')] += 1.
            
            key = tuple(count)
            #If the count is already in the dictionary, then the word will be appended
            #Otherwise, a new key-value pair will be created with the count as the key and the word as the first value, 
            # this is also why we need the dict to be a defaultdict(list) - so it can append to the list
            anagramsDict[key].append(word)

        return anagramsDict.values()

#Time Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
#Space Complexity: O(n * k)
