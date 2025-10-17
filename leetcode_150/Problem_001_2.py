class Solution:
    def twoSum(self, nums, target):
        # Create an empty dictionary to store number and its index
        numMap = {}
        # Get the length of the input list nums
        n = len(nums)

        # Loop through each number to build the dictionary
        for i in range(n):
            # Store number as key and its index as value
            numMap[nums[i]] = i

        # Loop again to find if complement (target - current number) exists
        for i in range(n):
            # Calculate complement
            complement = target - nums[i]
            # Check if complement exists in dictionary and is a different index
            if complement in numMap and numMap[complement] != i:
                # Return the pair of indices where sum equals target
                return [i, numMap[complement]]

        # If no pair found, return empty list
        return []

# Create Solution object
obj1 = Solution()
# Call the twoSum method and print indices of numbers summing to target
print(obj1.twoSum([2,7,11,15],9))  # Output: [0, 1]
