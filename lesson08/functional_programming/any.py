nums = [0, False, 5, 0]
result = any(nums)  
print(result)

nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)
