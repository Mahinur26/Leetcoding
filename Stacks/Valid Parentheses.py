#Easy

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #Mapping each closed parentheses to open
        #Close:open parentheses
        closeToOpen = {")":"(", "}":"{", "]":"["}
        for char in s:
            #If the char is a key - closed parentheses
            if char in closeToOpen:
                #if stack isn't empty and checking the top char to see if it matches with the open parentheses
                if stack and (stack[-1] == closeToOpen[char]):
                    stack.pop()
                else:
                    return False
            #The char must be an open parentheses
            else:
                stack.append(char)
        #Means we looked through all the characters and they matched properly
        if not stack:
            return True
        else:
            return False