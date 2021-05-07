'''

1. Arrays: Print all sublists

Add each number to previous element (including empty list,
which will provide the [] case and [j] cases (individual numbers as sublists)

O(n * 2^n) time (exponential time): 
    n: iterate through every element in list
    2^n: in 2nd for loop, the list grows
'''
def sub_lists(l):
	lists = [[]]
	for i in range(len(l)):
		orig = lists[:]
		new = l[i]
		for j in range(len(lists)):
			lists[j] = lists[j] + [new]
		lists = lists + orig
	return lists

'''
2. Basic Hash Table: Two Number Sum

Problem: Return 2 numbers that equal the target sum or [].

Iterate through array looking for potential match and store
the number in a hash table if it's not a match

1. Create a basic hash table 
2. potentialMatch = targetSum - num
3. Lookup potentialMatch in hash table and return potentialMatch 
and num if found
4. If not found, store num in hash table, assign to True and continue

O(n) time: iterate through entire list 
O(n) space: store n numbers in the hash table
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
3. Binary Search

Return index of target element or -1

Key insight:
Search for element by repeatedly dividing the array in half and see if element in left/right half 

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
4. LinkedList: Reverse a linked list

1. Linked List node has a value and next pointer
2. currentPointer.next = previousNode
3. previousNode = currentNode, currentNode = nextNode

O(n) time: traverse each node in the list
O(1) space: no matter how big the list, always only storing previous, current, next nodes 
'''
class LinkedList:
	def __init__(self, value):
		self.value = value
		self.next = None
		
def reverseLinkedList(head):
	previousNode, currentNode = None, head
	while currentNode is not None:
		nextNode = currentNode.next
		currentNode.next = previousNode
		previousNode = currentNode
		currentNode = nextNode
	return previousNode

'''
5. Stacks: Balanced Brackets
Key insight: if there is a closed bracket, the previous bracket
(the last bracket on the stack) must be a matching open bracket,
else unbalanced

O(n) time: iterate through characters in a string
O(n) space: push characters to a stack 
'''
def balancedBrackets(string):
	openingBrackets = "([{"
	closingBrackets = ")]}"
	matchingBrackets = {")":"(", "]": "[", "}": "{"}
	stack = []
	
	for char in string: 
		if char in openingBrackets:
			stack.append(char)
		elif char in closingBrackets:
			if len(stack) == 0:
				return False
			if stack[-1] == matchingBrackets[char]:
				stack.pop()
			else:
				return False
	return len(stack) == 0

'''
6. Graphs: Breadth First Search: 
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
7. Graphs: Depth First Search
1. Call DFS on a root node - add root node to the final array 
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
8. Binary Tree: Max Depth
'''
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if lDepth > rDepth:
            return lDepth + 1
        else: 
            return rDepth + 1

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
'''
9. Binary Tree (each node has at most 2 child nodes): Node depths

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
10. Binary Search Tree: Traversal - in/pre/post order

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


'''
11. Quick Sort

Key ideas: 
	Sort numbers with respect to a pivot.

Key steps:
	if number at left is larger than pivot and number at 
	right pointer is smaller than the pivot, swap the two numbers

	if number at left pointer smaller than pivot, move pointer forward

	if number at right pointer is larger than the pivot, move pointer back
	
	Swap pivot with the right pointer (bc we chose the first number as pivot)

Steps:
1. choose a pivot, create left and right pointers 
2. move numbers < pivot to the left of the pivot 
3. move numbers > pivot, to the right of the pivot
4. pivot will be in it's final sorted position
5. apply on subarray of the left/right of the newly positioned pivot 

Time complexity:
worst case: O(n^2) time: if pivot extemely lopsided subarrays 
best case: if pivot cuts to 2 even subarrays
	when pivot divides array into half, then make log n calls of quicksort until
	reach. Performing O(log n) operations n times => O(n log n)
average case: O(n log n)
Space complexity: O(log n) because run quicksort recursively on the smaller subarray first

'''

def quickSort(array):
	quickSortHelper(array, 0, len(array) - 1)
	return array

def quickSortHelper(array, startIdx, endIdx):
	if startIdx >= endIdx:
		return
	pivotIdx = startIdx
	leftIdx = startIdx + 1 
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
			swap(leftIdx, rightIdx, array)
		if array[leftIdx] <= array[pivotIdx]:
			leftIdx += 1
		if array[rightIdx] >= array[pivotIdx]:
			rightIdx -= 1
	swap(pivotIdx, rightIdx, array)
	leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
	if leftSubarrayIsSmaller:
		quickSortHelper(array, startIdx, rightIdx - 1)
		quickSortHelper(array, rightIdx + 1, endIdx)
	else:
		quickSortHelper(array, rightIdx + 1, endIdx)
		quickSortHelper(array, startIdx, rightIdx - 1)

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]


'''
12. Merge Sort: 

Solution 1: Create copies of arrays to sort 

Key idea: 
Keep dividing array until get to 1 element arrays and 
merge them into sorted arrays until the entire array is sorted.

Time Complexity:
O(n log n) time: Each level takes O(n) time, and we have O(log n) levels because 
we continuously divide the arrays in half

O(n log n) space

Solution 2: Sort in place

'''
def mergeSort(array):
	if len(array) == 1:
		return array
	middleIdx = len(array) // 2
	leftHalf = array[:middleIdx]
	rightHalf = array[middleIdx:]
	return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
	sortedArray = [None] * (len(leftHalf) + len(rightHalf))
	k = i = j = 0
	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] < rightHalf[j]:
			sortedArray[k] = leftHalf[i]
			i += 1
		else:
			sortedArray[k] = rightHalf[j]
			j += 1
		k += 1
	while i < len(leftHalf):
		sortedArray[k] = leftHalf[i]
		i += 1
		k += 1
	while j < len(rightHalf):
		sortedArray[k] = rightHalf[j]
		j += 1
		k += 1
	return sortedArray
    