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

# Flatten binary tree 

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(n) space, n = number of nodes in Binary Tree
def flattenBinaryTree(root):
	# Basic way to flatten binary tree is to get nodes in order
	inOrderNodes = getNodesInOrder(root, [])
	# traverse list of nodes
	# exclude the final node because will already be connected 
	for i in range(0, len(inOrderNodes) - 1):
		leftNode = inOrderNodes[i]
		rightNode = inOrderNodes[i+1]
		leftNode.right = rightNode
		rightNode.left = leftNode
	return inOrderNodes[0]

def getNodesInOrder(tree, array):
	if tree is not None:
		getNodesInOrder(tree.left, array)
		array.append(tree)
		getNodesInOrder(tree.right, array)
	return array 


# O(n) time | O(d) space, d = depth of the tree (recursive calls)
# if balanced binary tree, then O(log (n)) space 
def flattenBinaryTree(root):
	# recursive function: update the left/right pointers of a node with 
	# the 1) right most node of the left sub-tree and the 
	#     2) left most node of the right sub-tree
	leftMost, _ = flattenTree(root)
	return leftMost
	
def flattenTree(node):
	if node.left is None:
		leftMost = node
	else:
		leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
		connectNodes(leftSubtreeRightMost, node)
		leftMost = leftSubtreeLeftMost
		
	if node.right is None: 
		rightMost = node
	else:
		rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
		connectNodes(node, rightSubtreeLeftMost)
		rightMost = rightSubtreeRightMost 
		
	return [leftMost, rightMost]
		
def connectdNodes(left, right):
	left.right = right
	right.left = left

# Cannot reduce time complexity because must traverse all the nodes 
# Can reduce space complexity to O(d), d = depth (height) of tree or O(log n), if balanced tree
# O(log n) means, as n increases exponentially, space increases linearly. 
# Ex. n = 10, 100, 1000, space = 1, 2, 3 
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) time | O(d) space, d = depth of the tree (recursive calls)
# if balanced binary tree, then O(log (n)) space 
def flattenBinaryTree(root):
	# recursive function: update the left/right pointers of a node with 
	# the 1) right most node of the left sub-tree and the 
	#     2) left most node of the right sub-tree
	leftMost, _ = flattenTree(root)
	return leftMost
	
def flattenTree(node):
	# return the left most node and right most node of flattened tree
	if node.left is None:
		leftMost = node
	else:
		# in left subtree recursively call flattenTree until get left most node 
		leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
		# to flatten tree, connect the current node to the 
		# right most node of left subtree 
		connect (leftSubtreeRightMost, node)
		leftMost = leftSubtreeLeftMost 
	if node.right is None:
		rightMost = node 
	else:
		# in right subtree recursively call flattenTree until get right most node 
		rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
		# connect current node to the left most node of the right subtree 
		connect(node, rightSubtreeLeftMost)
		rightMost = rightSubtreeRightMost
	
	return [leftMost, rightMost]

def connectNodes(left, right):
	left.right = right
	right.left = left

# Depth First Search 

class Node: 
	def __init__(self, name):
		self.name = name
		self.children = []

	def depthFirstSearch(self, array):
		"""
		O(v + e) time
		v = number of vertices (nodes) in graph		
		Visit all the vertices: O(v) time
		
		e = number of edges in graph
		call DFS on each child node. number of child nodes 
		is number of edge 
		
		O(v) space: array returned of length v
		And worst case v frames on call stack 
		"""
		# add the name of current node
		# to the list of searched or "visited" nodes
		array.append(self.name)
		# call DFS function for each child node 
		# of the current node
		# "visit" a node 
		for child in self.children:
			child.depthFirstSearch(array)
		# return the array of searched nodes 
		return array

# breadth first search
class Node:
	def __init__(self, name):
		self.name = name
		self.children = []

	# O(v + e) time, v = # of vertices, e = # of edges 
	# O(v) space, storing all the node names in final array and 
	# worst case of queue is all the nodes are children of the 
	# root node. So have O(v - 1) space in queue or O(v) space 
	def breadthFirstSearch(self, array):
		# initialize the queue 
		queue = [self]
		# iterate through the queue
		while len(queue) > 0:
			# pop each node from queue in FIFo
			# to get the current node 
			current = queue.pop(0)
			# add the name of current node to final array
			array.append(current.name)
			# add child nodes to the queue 
			for child in current.children:
				queue.append(child)
		# return the final array
		return array

# permutations
def getPermutations(array):
	permutations = []
	permutationsHelper(array, [], permutations)
	return permutations

def permutationsHelper(array, currentPermutation, permutations):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i+1:]
			newPermutation = currentPermutation + [array[i]]
			permutationsHelper(newArray, newPermutation, permutations)


# binary search tree - insertion, search, delete

class BST:
	
	def __init__(self, value):
		self.value = value 
		self.left = None
		self.right = None 

    # O(log n) time on average, because removing half the nodes at each node 
    # O(n) time in worst case if a chain of 1 child nodes 
    # O(1) space, implemented iteratively - no frames stored on the call stack 

	def insert(self, value):
		#what node are we at 
		currentNode = self
		while True:
			# explore the left subtree 
			if value < currentNode.value:
				if currentNode.left is None: 
					# create and insert a value in BST 
					currentNode.left = BST(value)
					break
				else:
					currentNode = currentNode.left
			else:
				if currentNode.right is None:
					currentNode.right = BST(value)
					break
				else:
					currentNode = currentNode.right
		return self 

    def contains(self, value):
		currentNode = self
		while currentNode is not None:
			# go to left side of the subtree 
			if value < currentNode.value:
				currentNode = currentNode.left
			# go to the right side of the subtree
			elif value > currentNode.value: 
				currentNode = currentNode.right
			# if the value is equal to current node's value, then found the node 
			else:
				return True
		# node not in BST 
		return False

    # O(log n) time on average, O(n) time worst, if chain of child nodes 
	# O(1) space 
	def remove(self, value, parentNode = None):
		# 1. find the node trying to remove 
		# 2. remove the node 
		currentNode = self
		while currentNode is not None:
			if value < currentNode.value:
				parentNode = currentNode
				currentNode = currentNode.left
			elif value > currentNode.value: 
				parentNode = currentNode 
				currentNode = currentNode.right
			else: 
				# 2 children nodes 
				# find the left most value of the right subtree 
				# replace current node with that value and remove that value 
				if currentNode.left is not None and currentNode.right is not None:
					currentNode.value = currentNode.right.getMinValue()
					# call the remove on current node 
					currentNode.right.remove(currentNode.value, currentNode)
				elif parentNode is None:
					if currentNode.left is not None:
						currentNode.value = currentNode.left.value
						currentNode.right = currentNode.left.right
						ccurrentNode.left= currentNode.left.left 
					elif currentNode.right is not None:
						currentNode.value = currentNode.right.value
						currentNode.left = currentNode.right.left
						currentNode.right = currentNode.right.right
					else: 
						# root node has no child nodes 
						currentNode.value = None 
				elif parentNode.left == currentNode:
					parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
				elif parentNode.right == currentNode:
					parentNode.right = currentNode.left if curretnnode.left is not None else currentNode.right
				break		
		return self

def getMinValue(self):
	currentNode = self
	while currentNode.left is not None:
		currentNode = currentNode.left
	return currentNode.value

# O(n log n) time, because sift down (O(log n) time) on n elements
# O(1) space
def heapSort(array):
	# build the max heap:
	# max heap: 
	# 	binary tree where first node (number) is the largest 
	# 	parent node is larger than the 2 child nodes
	# 	each level must be complete, except for last level which must have 
	# 		0 or 2 end nodes per parent node 
	buildMaxHeap(array)
	# start from end
	for endIdx in reversed(range(1, len(array))):
		# first number is the largest 
		# swap with the last number 
		# last number is now sorted
		# first to n - 1 numbers is now unsorted 
		swap(0, endIdx, array)
		# sift down the first number so that it gets to the right position
		siftDown(0, endIdx - 1, array)
	return array

def buildMaxHeap(array):
	firstParentIdx = (len(array) - 1) // 2
	for currentIdx in reversed(range(firstParentIdx + 1)): 
		siftDown(currentIdx, len(array) - 1, array)

def siftDown(currentIdx, endIdx, heap):
	childOneIdx = currentIdx * 2 + 1 
	while childOneIdx <= endIdx:
		childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1 
		if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx 
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currentIdx]:
			swap(currentIdx, idxToSwap, heap)
			currentIdx = idxToSwap
			childOneIdx = currentIdx * 2 + 1
		else: 
			break

def swap(i, j, array):
	array[j], array[i] = array[i], array[j]

# greedy algorithms: class photos 

# O(n log n) time | O(1) space, because sort in place 
def classPhotos(redShirtHeights, blueShirtHeights):
	# Greedy algorithms: make the locally optimal choice at each stage 
	# sort heights from tallest to shortest 
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
	# determine which shirt color in first row 
	# compare heights of the tallest person of each row. first row must have the shorter of the two.
	shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'
	for idx in range(len(redShirtHeights)):
		redShirtHeight = redShirtHeights[idx]
		blueShirtHeight = blueShirtHeights[idx]
		# if red shirts in first row, then red shirt height must be small than blue shirt height
		# if not, then not possible to take the class picture and return False 
		if shirtColorInFirstRow == 'RED':
			if redShirtHeight >= blueShirtHeight:
				return False
		else: 
			if blueShirtHeight >= redShirtHeight:
				return False
	return True
    