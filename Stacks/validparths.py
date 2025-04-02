class Solution:
    def isValid(self, s: str) -> bool:
        # need to ask some clarifying questions
        # perhaps creating a dictionary for each and its complement
        # we want to iterate through string, check if the char in the dictionary
        # stack = [] # idea is to store opening brackets in stack
        # brackets = {
        #     ')':'(',
        #     ']':'[',
        #     '}':'{'}

        # for i in s: # checks the elements in the string
        #     if i in brackets.values(): # check if bracket is the opening brackets
        #         stack.append(i) # push opening brackets into stack

        #     elif i in brackets: # check if bracket is the closing brackets
        #         if stack and stack[-1] == brackets[i]: # check if stack not null
        #         # check if the last element is closing brackets (accesses key value)
        #             stack.pop() # pops the stack
        #         else: # if the last element is not closing bracket
        #             return False
        # return stack == [] # should be empty
        # return True if not stack else False # stack should be empty
        # since opening brackets are cancelled out by closing brackets
        # thus when stack not empty then unclosed brackets remain
        # not stack ~ not [] ~ not empty? ~ not false  == true
        # if not ['{',']'] ~ not empty? ~ not true == false

        # time complexity: O(n) for checking each parenthesis
        # space complexity: O(n) for storing and popping elements in stack

        #alternative implementation without dictionary/hashmap
        stack = [] # storing and checking matching
        
        for char in s:
            if char == '(' or char == '[' or char == '{':  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack:  # No matching opening bracket
                    return False
                
                top = stack.pop()
                # Check if the closing bracket matches the most recent opening bracket
                if ((char == ')' and top != '(') or
                    (char == ']' and top != '[') or
                    (char == '}' and top != '{')):
                    return False
        
        return len(stack) == 0  # True if stack is empty (all brackets matched)
        
        # time complexity: O(n)
        # space complexity: O(n)


