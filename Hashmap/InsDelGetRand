#380

# first implementation - Not all functions run O(1) time complexity
# removing a specific element from an array requires O(n) time

# import random

# class solution:
    
#     def __init__(self):
#         self.map = set()
        
#     def add(self, val):
#         self.map.add(val)
#         # O(1) time complpexity
#     def remove(self, val):
#         self.map.remove(val)
#         # O(n) time complpexity
#     def getRandom(self):
#         list_map = list(self.map)
#         x = len(list_map)
#         randomval = random.randint(0,x-1)
#         print(list_map[randomval])
#         # O(1) time complpexity
#     def printSet(self):
#         print(list(self.map))
        
# correct implementation utilizing hashmap and stack        
class RandomizedSet:

    def __init__(self):
        self.values = []
        self.valuesIdx = {} # value: index

    def insert(self, val: int) -> bool:
        if val in self.valuesIdx:
            return False
        
        self.valuesIdx[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valuesIdx:
            return False
        
        index = self.valuesIdx[val]
        self.valuesIdx[self.values[-1]] = index
        del self.valuesIdx[val]
        self.values[index] = self.values[-1]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self.values) - 1)
        return self.values[index]
        return self.values[index]
