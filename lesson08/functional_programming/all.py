nums = [1, 2, 3, 4]
result = all(nums)  
print(result)


nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even)

words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)
