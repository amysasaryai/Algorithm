def findMin(nums):
  pivot = True
  i = 0
  while pivot and i <= len(nums)-2:
    if nums[i] > nums[i+1]:
      pivot = False
    i = i+1

  if nums[i] < nums[0]:
    return nums[i]
  else: return nums[0]


print findMin([4,5,6,7,8,9,3,4,5])

