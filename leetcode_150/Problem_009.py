class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x
    
# ✅ Create object and test
obj = Solution()

# Example number
num = 121

# Call the function and print result
print("Is Palindrome:", obj.isPalindrome(num))
