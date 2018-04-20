def twoSum(self, nums, target):
    maporder = dict()
    for order in range(len(nums)):
        if nums[order] not in maporder.keys():
            maporder[nums[order]] = [order]
        else:
            maporder[nums[order]].append(order)

    for key in maporder.keys():
        if (target - key) == key and len(maporder[key]) == 2:
            return [maporder[key][0], maporder[key][1]]
        elif (target - key) in maporder.keys():
            return [maporder[key][0], maporder[target-key][0]]
