numbers = [1, 2, 3, 4, 5]
for i in map(lambda x: x ** 2, numbers):
    print(i)

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)
print(list(sum_nums))
