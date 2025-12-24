nums = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list : {nums}")

nums = nums[0:5:1]
print(f"Extracted first five elements : {nums}")


nums.sort(reverse=True)
print(f"Reversed extracted elements : {nums}")