#Medium
#Must implament a 0(1) time complexity solution
#Thus another minStack needed to be initialized
class MinStack:

    def __init__(self):
        self.stack = []
        #Create another stack to mirror the noraml stack, but with min values toppling on each other
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        #If the val being pushed isn't less than the top val/min in minStack, then we add the top val again to the top
        #This way, when we pop the top will always have the min value for as long as it exists the main stack
        elif(val<self.minStack[-1]):
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]