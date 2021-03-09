'''
Basic Hash Table: Two Number Sum

Problem: Return 2 numbers that equal the target sum or [].

Iterate through array looking for potential match and store
the number in a hash table if it's not a match

1. Create a basic hash table 
2. potentialMatch = targetSum - num
3. Lookup potentialMatch in hash table and return potentialMatch and num if found
4. If not found, store num in hash table, assign to True and continue
'''

def twoNumberSum(array, targetSum):
	nums = {}
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		nums[num] = True
	return []

'''
Binary Search

Return index of target element or -1

Recursive Solution:
Repeatedly divide the array in half and see if the target is in the right 
or left half of the array

1. Left/Right pointers at beginning/end of array
2. Check base case of empty array: left index > right index 
3. Compute the floor of middle index
4. Store the potential match
5. 3 cases
	a. target == potentialMatch
	b. target < potential match => look (recursive call) in left half of array
	c. target > potential match => look in right half of array

Time/Space Complexity: 

O (log n) time: eliminate 1/2 of elements in each iteration
O (log 1) space: don't store anything
'''

def binarySearch(array, target):
	return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
	if left > right:
		return -1
	middle = (left + right) // 2
	potentialMatch = array[middle]
	if target == potentialMatch:
		return middle
	elif target < potentialMatch:
		return binarySearchHelper(array, target, left, middle - 1)
	else: 
		return binarySearchHelper(array, target, middle + 1, right)

'''
Graphs: Breadth First Search: 
1. Add root node to the queue
2. Pop node from front of the queue, assign to current node
3. Add current node name to final list of nodes
4. Add children nodes to queue
5. Repeat 2 - 4

O(V + E) time: 
	O(V), V = vertex: traverse all nodes (vertices), add each to current node 
	O(E), E = edge: add child nodes to queue
O(V) space: in worst case, queue of child nodes hold V - 1 nodes
	if all children nodes coonnected to 1 parent, then V - 1 nodes in queue
'''
class Node:
	def __init__(self, name): 
		self.name = name
		self.children = []
		
	def breadthFirstSearch(self, array):
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			array.append(current.name)
			for child in current.children:
				queue.append(child)
		return array

'''
Graphs: Depth First Search
1. Call DFS on a root node 
2. Add node to the final array
3. Call DFS on each child node 
4. Repeat 

O(V+E) time, V = vertices, E = Edges: traverse all the vertices and for each vertex, we also 
traverse all the child nodes (edges)

O(V) space: in the worst case, we are adding V frames to the call stack, 
if each node only has one child node and we have a long string of nodes. 
A - B - C - D - E ... 
'''
class Node:
	def __init__(self, name):
		self.name = name
		self.children = []
		
	def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array

'''
Binary Tree (each node has at most 2 child nodes): Node depths

Problem: Return the sum of depths of all nodes in a binary tree

Recursive Solution:
1. Base case: if no child node, return 0 
2. Pass current node depth + 1 to left and right nodes

O(n) time: traverse through every node in the binary tree and perform constant time operations on each node 
O(h) space, h = height of binary tree: maxiumum number of function calls on the call stack at one time is h
For balanced tree, approaches O(log n) because eliminating 1/2 of nodes at each sub tree 
'''
def nodeDepths(root, depth=0):
	if root is None:
		return 0
	return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# iterative solution
# O(n) time: traverse each node in tree
# O(h) space: max nodes in stack is roughly height of the tree
def nodeDepths(root):
	# track the sum of depths
	sumOfDepths = 0
	# create a stack of nodes to track depths
	stack = [{"node": root, "depth": 0}]
	# traverse the binary tree
	while len(stack) > 0:
		# pop node off the stack
		nodeInfo = stack.pop()
		# get the node, depth
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		# account for empty child node
		if node is None:
			continue
		sumOfDepths += depth
		# push child nodes onto the stack
		stack.append({"node": node.left, "depth": depth + 1})
		stack.append({"node": node.right, "depth": depth + 1})
	return sumOfDepths

'''
Binary Search Tree: Traversal - in/pre/post order

In order:
1. get nodes from left to right of the tree 
2. call inOrder function passing in left child, append value, call inOrder function passing in right child

Pre order: 
1. root node, left subtree, right subtree
2. append value, call preOrder passing in left child, call preOrder passing in right child

Post order: 
1. left subtree, right subtree, then root 
2. call postOrder with left child, postOrder with right child, append value

O(n) time | O(n) space, if not array accum, then O(d), d is depth of tree 
'''

def inOrderTraverse(tree, array):
	if tree is not None:
		inOrderTraverse(tree.left, array)
		array.append(tree.value)
		inOrderTraverse(tree.right, array)
	return array

def preOrderTraverse(tree, array):
	if tree is not None:
		array.append(tree.value)
		preOrderTraverse(tree.left, array)
		preOrderTraverse(tree.right, array)
	return array

def postOrderTraverse(tree, array):
	if tree is not None:
		postOrderTraverse(tree.left, array)
		postOrderTraverse(tree.right, array)
		array.append(tree.value)
	return array

# two number sum

# hash table method 
# O(n) time: traversing through each element in the array
# O(n) space: hash table to track the traversed elements 
def twoNumberSum(array, targetSum):
	# x + y = target 
	# y = target - x
	# traverse the array looking for y
	# track traversed elements in hash table
	nums = {}
	for num in array:
		# y = target - x
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch, num]
		else:
			nums[num] = True
	return []

# sort first, then use 2 pointers
# O(n log n ) time: sort is log n time, traverse through n elements  
# 	n log n + n => n(log n + 1) => O (n log n) time 
# O(1) space: don't use additional space

# sort the array first, then set 2 pointers
def twoNumberSum(array, targetSum):
	# sort the array first
	array.sort()
	# initialize the two pointers 
	left = 0
	right = len(array) - 1
	while left < right:
		# compute potential match
		potentialMatch = array[left] + array[right]
		if potentialMatch == targetSum:
			return [array[left], array[right]]
		# need a larger number, so move left pointer up
		elif potentialMatch < targetSum:
			left += 1
		# need a smaller number, so move right pointer back
		elif potentialMatch > targetSum:
			right -= 1
	# didn't find the target sum
	return []

# Quick Sort 
# Time complexity 
# worst case: O(n^2) time: if pivot extemely lopsided subarrays 
# best case: if pivot cuts to 2 subarrays
# 	when pivot divides array into half, then make log n calls of quicksort until
#	reach. Performing O(log n) operations n times => O(n log n)
# average case: O(n log n)
# Space complexity: O(log n) because run quicksort recursively on the smaller subarray first
def quickSort(array):
	quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	# base case 
	if startIdx >= endIdx:
		return
	# choose first index to simplify 
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx 
	while rightIdx >= leftIdx:
		# swap, inc/dec right/left pointers
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1

	swap(pivotIdx, rightIdx, array)
	# now pivot is in the correct position
	# recursive call first on the smaller subarray to minimize space complexity
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)
	
def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
