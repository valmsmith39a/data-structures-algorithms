# Find equilibrium index of an array: left and right sums are the same


def equilibriumIndex(arr):
    right = 0
    leftover = 0
    equilibIndex = 0
    total = sum(arr)
    for i in range(len(arr)-1, -1, -1):
        leftover = total - (arr[i] + right)
        right += arr[i]
        if right == leftover:
            return i


arr = [1, 2, 3, 5, 7, 9, 10, -1]
print(equilibriumIndex(arr))

# Given an array nums and a value val, remove all instances of that value in-place and return the new length.


def removeElement(self, nums: List[int], val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


def isPalindrome(self, x: int) -> bool:
    return str(x) == str(x)[::-1]

# max profit k transactions
# O(nk) time | O(nk) space

def maxProfitWithKTransactions(prices, k):
	# check for empty prices array
	if not len(prices): 
		return 0
	# create the 2D array of profits 
	profits = [[0 for d in prices] for t in range(k+1)]
	# iterate through the 2D array of profits
	# start with the rows
	for t in range(1, k + 1):
		# keep track of max profit from 1 transaction up to this point
		# initialize to the smallest possible value in Python
		maxThusFar = float("-inf")
		for d in range(1, len(prices)):
			# max of 
			# 1. do nothing, so get the previous day's profits
			# 2. sell, so get today's sell price + max profit from 1 transaction 
			# Keep track of max profit from 1 transaction up to this point
			maxThusFar = max(maxThusFar, profits[t-1][d-1] - prices[d-1])
			profits[t][d] = max(profits[t][d-1], prices[d] + maxThusFar)
	
	return profits[-1][-1]

# Reduce space complexity from O(nk) to O(n)
def maxProfitWithKTransactions(prices, k):
	# check for empty prices array
	if not len(prices):
		return 0
	# initialize 2 profit rows that are used (n columns, 2 rows)
	# instead of the entire prices matrix (n columns, k rows)
	# this is the key to reducing space complexity
	evenProfits = [0 for d in prices]
	oddProfits = [0 for d in prices]
	# iterate through k rows and d prices 
	# skip the first row becaue it's 0s
	for t in range(1, k + 1):
		# initialize to smallest possible value
		maxThusFar = float("-inf")
		# swap current profit and previous profit 
		# odd case 
		if t % 2 == 1: 
			currentProfits = oddProfits
			previousProfits = evenProfits
		# even case
		else: 
			currentProfits = evenProfits
			previousProfits = oddProfits
		# iterate through rices
		for d in range(1, len(prices)):
			# max profit comparing buying at each element in prices array
			maxThusFar = max(maxThusFar, previousProfits[d - 1] - prices[d - 1])
			# either you:
			# (1) don't sell on the current day and make previous day's profits
			# (2) sell on the current day and make sale price + maxThusFar
			currentProfits[d] = max(currentProfits[d-1], maxThusFar + prices[d])
	# return even profits if even row, odd profits if odd row 
	return evenProfits[-1] if t % 2 == 0 else oddProfits[-1]

# apartment hunting
# O(b^2 * r + b) => b * (br + 1) => O(b^2r)) time
# O(b) space
# find the block that is the closest to all required buildings
def apartmentHunting(blocks, reqs):
	# track max distance from a block to a required building 
	# at each block 
	maxDistancesAtBlocks = [float("-inf") for block in blocks]
	# find the minimum distance between a required building and block
	# traverse the blocks
	for i in range(len(blocks)):
		# find the closest required distance for each required building
		for req in reqs:
			closestReqDistance = float("inf")
			# traverse blocks to find the closest required distance 
			for j in range(len(blocks)):
				# required building exists at block
				if blocks[j][req]:
					# i: index at current block
					# j: index of block for a required building 
					closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
			maxDistancesAtBlocks[i] = max(maxDistancesAtBlocks[i], closestReqDistance)
	# return the index of block with the smallest max distance to a required building
	return getIdxAtMinValue(maxDistancesAtBlocks)

def distanceBetween(a, b): 
	return abs(a - b)

def getIdxAtMinValue(array):
	# track index at min value
	idxAtMinValue = 0
	# track min value 
	minValue = float("inf")
	# traverse array to find the min value
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue

# apartment hunting reduce from O(b^2 * r) time to O(br) time 

def apartmentHunting(blocks, reqs):
	minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
	maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
	pass

def getMinDistances(blocks, req):
	minDistances = [0 for block in blocks]
	closestReqIdx = float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqIdx = i
		minDistances[i] = distanceBetween(i, closestReqIdx)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIdx = i
		minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
	return minDistances
	
def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
	maxDistancesAtBlocks = [0 for block in blocks]
	for i in range(len(blocks)):
		minDistancesAtBlock = list(map(lambda distances: distances[i] + 5, minDistancesFromBlocks))
		maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
		
def distanceBetween(a, b):
	return abs(a-b)

# apartment hunting with improved time complexity, worse space complexity 
# 2*O(br) + O(b) => O(br + b) => O(b(r + 1)) => O(br) time
# O(br + b) => O(b(r + 1)) => O(br) space 
def apartmentHunting(blocks, reqs):
	# for each required building, precompute the 
	# min distance from each block
	# Ex 
	# gym: [0, 0, 1, 1, 0]
	# store: [1, 2, 2, 1, 0]
	minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req) , reqs)) #O(br)
	# from all the min distances from blocks, get the max distance 
	maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks) #O(br)
	return getIdxAtMinValue(maxDistancesAtBlocks) #O(b * (r + 1)) => O(br)

# O(r): map over the required buildings 
# 3O(b) -> O(b): min distances, 2 for loops
# O(r) * O(b) => O(br)
def getMinDistances(blocks, req):
	# min distances from each block to required building 
	minDistances = [0 for block in blocks]
	closestReqIdx = float("inf")
	# iterate through blocks and get the min distance from each block to req building
	# iterate left to right first to get the min distance from each block to req building
	for i in range(len(blocks)):
		# track the index of the closest required building 
		if blocks[i][req]:
			closestReqIdx = i
		minDistances[i] = distanceBetween(i, closestReqIdx)
	# iterate right to left to get the min distance from each block to req building 
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqIdx = i
		# want the minimum between what we found above and current calculation
		minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
	return minDistances

# O(b): initialize the maxDistancesAtBlocks
# O(b): for loop through the blocks 
# O(r): minDistancesFromBlocks is array of length r 
# O(b) + O(br) => O(b(1 + r)) => O(br)
def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
	# find the maximum distance of all the nearest distances to each block
	maxDistancesAtBlocks = [0 for block in blocks]
	for i in range(len(blocks)):
		# for each required building, get the min distance at each block 
		minDistancesAtBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
		# get the max distance from the list of min distances at each block 
		maxDistancesAtBlocks[i] = max(minDistancesAtBlock)
	return maxDistancesAtBlocks 

def distanceBetween(a, b): 
	return abs(a - b)

def getIdxAtMinValue(array):
	# track index at min value
	idxAtMinValue = 0
	# track min value 
	minValue = float("inf")
	# traverse array to find the min value
	for i in range(len(array)):
		currentValue = array[i]
		if currentValue < minValue:
			minValue = currentValue
			idxAtMinValue = i
	return idxAtMinValue

    
# calendar 
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	# update calendars to account for artificial meetings 
	updatedCalendar1 = updateCalendar(calendar1, dailyBounds)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)

def updatedCalendar(calendar, dailyBounds):
	updatedCalendar = calendar[:]
	updatedCalendar.insert(0, ['0:00', dailyBounds[0]])
	updatedCalendar.append([dailyBounds[1]], '23:59')
	return list(map(lambda m: timeToMinutes(m[0]), timeToMinutes(m[1])), updatedCalendar)

	
def timeToMinutes(time): 
	hours, minutes = list(map(int, time.split(':')))
	
timeToMinutes('23:59')

# O(c1 + c2) time | O(c1 + c2) space
def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
	# update calendars to account for artificial meetings
	updatedCalendar1 = updateCalendar(calendar1, dailyBounds1)
	updatedCalendar2 = updateCalendar(calendar2, dailyBounds2)
	mergedCalendar = mergeCalendars(updatedCalendar1, updatedCalendar2)
	flattenedCalendar = flattenCalendar(mergedCalendar)
	return getMatchingAvailabilities(flattenedCalendar, meetingDuration)

# always O(c1) + O(c2) time | at most O(c1) + O(c2) space
def mergeCalendars(calendar1, calendar2):
	# merge calendars using merge sort algorithm
	merged = []
	# i to track calendar 1 
	# j to track calendar 2
	i, j = 0, 0
	while i < len(calendar1) and j < len(calendar2):
		meeting1, meeting2 = calendar1[i], calendar2[j]
		if meeting1[0] < meeting2[0]:
			merged.append(meeting1)
			i += 1
		else:
			merged.append(meeting2)
			j += 1

	while i < len(calendar1): 
		merged.append(calendar1[i])
		i += 1
		
	while j < len(calendar2): 
		merged.append(calendar2[j])
		j += 1
	return merged 

# always O(c1) + O(c2), at most O(c1) + O(c2) space
def flattenCalendar(calendar): 
	# find all the values of calendar that overlap
	# [0, 120]
	# better to make a copy 
	flattened = [calendar[0][:]]
	for i in range(1, len(calendar)):
		currentMeeting = calendar[i]
		previousMeeting = flattened[-1]
		currentStart, currentEnd = currentMeeting
		previousStart, previousEnd = previousMeeting
		if previousEnd >= currentStart:
			newPreviousMeeting = [previousStart, max(previousEnd, currentEnd)]
			# print('new previous meeting', newPreviousMeeting)
			# print('flattened before', flattened)
			flattened[-1] = newPreviousMeeting
			# print('flattened after', flattened)
		else: 
			flattened.append(currentMeeting[:])
	return flattened

def updateCalendar(calendar, dailyBounds):
	# copy the calendar to avoid mutating originatl input
	# O(c)
	updatedCalendar = calendar[:]  
	# insert additional busy time range
	updatedCalendar.insert(0, ['0:00', dailyBounds[0]])
	updatedCalendar.append([dailyBounds[1], '23:59'])
	# transform the string values to numeric values, representing the mintues 
	# these values hold to compare times 
	# O(c1) + O(c2)
	return list(map(lambda m: [timeToMinutes(m[0]), timeToMinutes(m[1])], updatedCalendar))

def getMatchingAvailabilities(calendar, meetingDuration):
	matchingAvailabilities = []
	for i in range(1, len(calendar)):
		# start time is the end time of the previous meeting
		start = calendar[i-1][1]
		# end time is the start time of the current meeting (i)
		end = calendar[i][0]
		# beginning of next meeting (end time) - end of the current meeting (beginning time)
		availabilityDuration = end - start
		if availabilityDuration >= meetingDuration:
			matchingAvailabilities.append([start, end])
	return list(map(lambda m: [minutesToTime(m[0]), minutesToTime(m[1])], matchingAvailabilities))

# O(1) time | O(1) space
def timeToMinutes(time): 
	hours, minutes = list(map(int, time.split(':')))
	# convert to minutes
	return hours * 60 + minutes

# O(1) time | O(1) space 
def minutesToTime(minutes): 
	# Python will round down (flooring) the value 
	hours = minutes // 60
	# minutes modulo 60
	mins = minutes % 60
	hoursString = str(hours)
	minutesString = '0' + str(mins) if mins < 10 else str(mins)
	return hoursString + ':' + minutesString
