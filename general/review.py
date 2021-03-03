
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
