
# return the sum of depths of all nodes in a binary tree

# recursive solution
# O(n) time: traverse through every node in the tree and perform constant time operation on each node 
# O(h) space, h = height of binary tree: maximum number of function calls on a call stack at one point is h
# For balanced tree, approaches O(log n) because eliminating 1/2 of nodes at each subtree 
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

# binary search tree traversal in/pre/post

# O(n) time | O(n) space, if not array accum, then O(d), d is depth of tree 
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
