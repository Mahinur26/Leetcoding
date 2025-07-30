#Medium

#My solution/less efficient solution:
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mapOfAnagrams = {} #sortedWord tuple: Word str
        for word in strs:
            #Lists aren't hashable, but tuples are as they are immutable
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