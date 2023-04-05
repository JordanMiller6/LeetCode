class Solution:
    @staticmethod
    def romanToInt(s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        prev_value = 0
        
        for i in range(len(s)-1, -1, -1):
            curr_value = roman_dict[s[i]]
            if curr_value < prev_value:
                result -= curr_value
            else:
                result += curr_value
            prev_value = curr_value
        
        return result

# driver code
def main():
    s = "III"
    print(Solution.romanToInt(s)) # Output: 3
    
    s = "LVIII"
    print(Solution.romanToInt(s)) # Output: 58
    
    s = "MCMXCIV"
    print(Solution.romanToInt(s)) # Output: 1994

if __name__ == '__main__':
    main()
