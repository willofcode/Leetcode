class Solution:
    def romanToInt(self, s: str) -> int:
        # the objective of roman to integer is to map the value of roman numeral to integer val
        # what are some constraints to consider?
        # can there be non-char?
        # perhaps store the values to dictionary
        # initialize integer output
        # iterate through s
        # check the first element and compare with second element,
        # if first < second then set output - first element
        # else first > second then set output + first

        # first implementation

        Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # mapped the roman to int
        n = len(s) # lenght of string
        res = 0
        for i in range(n):
            if i == n - 1: # handles edge cases when there is only one element in s
                res += Roman[s[i]] # add the converted value from mapped dictionary
            else:
                if Roman[s[i]] < Roman[s[i + 1]]: # coverts the char into value and compare
                    res -= Roman[s[i]] # when first char < second char
                else:
                    res += Roman[s[i]] # when first char > second char
        return res

        # alternative Implementation

        # Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # mapped the roman to int
        # n = len(s)
        # res = Roman[s[n - 1]] # initialize and convert the last element of S
        # # this implementation checks from right to left
        # for i in range(n - 2, -1, -1): # start at the second to last, stop at 0, decrement by -1
        #     if Roman[s[i]] < Roman[s[i + 1]]: # coverts the char into value and compare
        #         res -= Roman[s[i]]
        #     else:
        #         res += Roman[s[i]]
        # return res

        # time complexity: O(n)
        # space complexity: O(1)

        # mapping the whole entire range to be mapped would be inefficient to just reduce time
        # the tradeoff in not balance as it requires more memeory and preprocessing power

        # Optimize implementation

        # 1994 = "MCMXCIV" = "VICXMCM" = 5 1 100 10 1000 100 1000
        # curr = 5
        # res = 0 + 5
        # prev = 5
        # curr = 1
        # res = 5 - 1 = 4
        # prev = 1
        # ...

        # Roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # mapped the roman to int
        # n = len(s) # length of string
        # s = s[::-1] # reverse the string
        # res = 0
        # prevval = 0 # track prevval
        # for char in s:
        #     currval = Roman[char] # convert char into integer via dictionary
        #     if currval < prevval: # condition for when curr val is less than
        #         res -= currval
        #     else:
        #         res += currval
        #     prevval = currval # updates current to previous

        # return res



     
