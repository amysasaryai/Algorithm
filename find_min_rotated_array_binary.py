def findMin(nums):
	n = len(nums)
	start, end = 0, n - 1
	if nums[start] <= nums[end]:
		return nums[start]
	else:
		while start <= end:
			mid = (start + end) // 2
			if nums[mid-1] > nums[mid] < nums[(mid + 1) % n]:
				return nums[mid]
			elif nums[mid] <= nums[end]:
				end = mid - 1
			else:
				start = mid + 1



print findMin([1,0])


