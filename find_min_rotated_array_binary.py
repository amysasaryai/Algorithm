def findMin(nums):
  pivotfound = False
  first = 0
  last = len(nums)-1
  item = nums[0]
  while first <= last and not pivotfound:
    midpoint = (first + last)//2
    if nums[midpoint] < item and nums[midpoint-1] > item:
        pivotfound = True
        return nums[midpoint]
    elif nums[midpoint] < item and nums[midpoint-1] < item: 
        last = midpoint - 1
        item = nums[midpoint-1]
    elif nums[midpoint] > item:
        first = midpoint + 1


print findMin([4,5,6,7,8,1,2,3])


