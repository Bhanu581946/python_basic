# 👇 Class definition (LeetCode style)
class Solution:
    
    # Function to check if a number is palindrome or not
    # x: int → input number,  returns bool → True/False
    def isPalindrome(self, x: int) -> bool:
        
        # Agar number negative hai (-121 etc.), to palindrome nahi ho sakta
        if x < 0:
            return False
        
        # rev variable reverse number store karega
        rev = 0
        
        # num me original number ki copy rakhi gayi hai (x ko directly change nahi karte)
        num = x
        
        # Jab tak num 0 nahi hota, tab tak loop chalta rahega
        while num != 0:
            # Last digit nikalte hain aur reverse me add karte hain
            # Example: rev = rev*10 + (num ka last digit)
            rev = rev * 10 + num % 10
            
            # num ko 10 se divide karke last digit hata dete hain
            num = num // 10
        
        # Agar reverse number original ke barabar hai → palindrome hai
        return rev == x
    

# ✅ Create object of class
obj = Solution()

# Example number jise check karna hai
num = 121

# Function call karo aur result print karo
print("Is Palindrome:", obj.isPalindrome(num))
