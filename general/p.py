def twoNumberSum(array, targetSum): 
	nums = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		nums[num] = True
