# 4. Найти максимальное из n чисел

def max_of_numbers(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum


numbers = [3, 4, 8, -2, 4]
print(max_of_numbers(numbers))
print(max(numbers))
