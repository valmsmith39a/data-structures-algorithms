"""
Key concepts:

1. logarithm
    log base 2 n = y 
    2^y = n 
    as n doubles (2, 4, 8, 16, 32)
    n only increases by 1 (1, 2, 3, 4, 5)
"""

"""

1. Arrays: Print all sublists

Add each number to previous element (including empty list,
which will provide the [] case and [j] cases (individual numbers as sublists)

O(n * 2^n) time (exponential time): 
    n: iterate through every element in list
    2^n: in 2nd for loop, the list grows
"""


def sublists(l):
    lists = [[]]
    for i in range(len(l)):
        prev_lists = lists[:]
        new_list = l[i]
        for j in range(len(lists)):
            lists[j] = lists[j] + [new_list]
        lists = lists + prev_lists
    return lists


# test_list = [1, 2, 3]
# print(sublists(test_list))
# [[1, 2, 3], [2, 3], [1, 3], [3], [1, 2], [2], [1], []]

"""
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
"""


def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [num, potentialMatch]
        nums[num] = True
    return []


# test = [1, 2, 5, 6, 8, 20, 3]
# print(twoNumberSum(test, 23))
# print(twoNumberSum(test, 59))
# [3, 20]
# []

"""
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
O (1) space: don't store anything

"""


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


# array = [2, 4, 6, 7, 8, 9, 12]
# target = 6
# print(binarySearch(array, target))


"""
4. LinkedList: Reverse a linked list

1. Linked List node has a value and next pointer
2. currentNode.next = previousNode
3. Traverse the linked list: 
    previousNode = currentNode, 
    currentNode = nextNode

O(n) time: traverse each node in the list
O(1) space: no matter how big the list, always only storing previous, current, next nodes 
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(node):
    previousNode, currentNode = None, node

    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode


# node = LinkedList(1)
# node.next = LinkedList(2)
# node.next.next = LinkedList(3)
# currentNode = node


# def printNodes(node):
#     while node is not None:
#         print(node.value)
#         node = node.next


# printNodes(currentNode)

# currentNode = reverseLinkedList(node)

# printNodes(currentNode)

"""
5. Stacks: Balanced Brackets

Stack: Last In First Out 

Key insights: 
    1. if there is a closed bracket, the previous bracket
    (the last bracket on the stack) must be a matching open bracket,
    else unbalanced. 

    2. if the string has balanced brackets, then after iterating through the string
    the stack should be empty

O(n) time: iterate through characters in a string
O(n) space: push characters to a stack 
"""


def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
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


"""
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
"""


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


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# n1.children = [n2, n3]
# n2.children = [n4, n5]

# array = []

# print(n1.breadthFirstSearch(array))


"""
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
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(6)
# n7 = Node(7)

# n1.children = [n2, n3]
# n2.children = [n4, n5]
# n4.children = [n6]
# n5.children = [n7]

# array = []

# print(n1.depthFirstSearch(array))

"""
8. Binary Tree: Depth or Height of Tree

Height of binary tree: Total number of nodes from root now to leaf node (including root and leaf nodes)
       
        1

Height of tree with 1 node: 1 

        1
    2       3
4       5


Height: 3
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


n0 = BinaryTree(0)
n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)

n0.left = n1
n0.right = n2
n1.left = n3
n1.right = n4

# Solution: 3
print("height of tree is: ", height(n0))

"""
9. Binary Tree (each node has at most 2 child nodes): Node depths

Problem: Return the sum of depths of all nodes in a binary tree

Recursive Solution:
1. Base case: if no child node, return 0 
2. Pass current node depth + 1 to left and right nodes

O(n) time: traverse through every node in the binary tree and perform constant time operations on each node 
O(h) space, h = height of binary tree: maxiumum number of function calls on the call stack at one time is h
For balanced tree, approaches O(log n) because eliminating 1/2 of nodes at each sub tree 
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


# n0 = BinaryTree(0)
# n1 = BinaryTree(1)
# n2 = BinaryTree(2)
# n3 = BinaryTree(3)
# n4 = BinaryTree(4)
# n5 = BinaryTree(5)
# n6 = BinaryTree(6)
# n7 = BinaryTree(7)
# n8 = BinaryTree(8)

# n0.left = n1
# n0.right = n2
# n1.left = n3
# n1.right = n4
# n2.left = n5
# n2.right = n6
# n3.left = n7
# n3.right = n8
# # 16
# depth = 0
# print(nodeDepths(n0, depth))

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


"""
10. Binary Search Tree: Traversal - in/pre/post order


Inorder traversal: 

                              1
			    2				            3
		4		       5		    6		        7
8	        9 	10 	        11 12        13 14             15

Start from the bottom of the tree.

Inorder Traversal: Left subtree (can be single node), Root, Right subtree
8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15

Preorder Traversal: Root, Left subtree, Right subtree
1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15

Postorder Traversal: Left subtree, Right subtree, Root
8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1

O(n) time | O(n) space, if not array accum, then O(d), d is depth of tree 
"""


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


"""
11. Quick Sort

Key ideas: 
	Sort numbers with respect to a pivot.
    Move numbers <= pivot to the left of the pivot.
    Move numbers > pivot to the right of the pivot

Key steps:
    With each iteration, ask: is number at left pointer larger than the pivot and the numer at 
    the right pointer smaller than the pivot? If it is, swap the numbers at the left pointer and right pointer.
    if number at left pivot is smaller than pivot, move pointer forward
    if number at right pointer is larger than pivot, move pointer back 
    When left pointer index > right pointer index, swap number at pivot index with number at right pointer index.

Steps:
    1. choose a pivot, create left and right pointers 
    2. move numbers < pivot to the left of the pivot 
    3. move numbers > pivot, to the right of the pivot
    4. pivot will be in it's final sorted position
    5. apply on subarray of the left/right of the newly positioned pivot 

Example - after completion of while loop:
    [4, 1, 2, 3, 5, 6, 7, 8]
    pivotIdx = 0
    rightIdx = 3
    leftIdx = 4

    pivotNumber = 4
    rightIdxNumber = 3
    leftIdxNumber = 5

    After iterating through the while loop, the value at the rightIdx is 
    the last number that is smaller than the pivot value.

    Since we know that the value at the rightIdx is smaller than the 
    pivot value, we can swap those 2 values. 

    [3, 1, 2, 4, 5, 6, 7, 8]

    Time complexity:
    worst case: O(n^2) time: if pivot extemely lopsided subarrays 
    best case: if pivot cuts to 2 even subarrays when pivot divides array into half, then make log n calls of quicksort until reach. Performing O(log n) operations n times => O(n log n)
    average case: O(n log n)
    Space complexity: O(log n) because run quicksort recursively on the smaller subarray first
"""


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
    # rightIdx and leftIdx have crossed
    # number at rightIdx is the last number that is smaller that the pivot number
    swap(pivotIdx, rightIdx, array)

    # at this point, the pivot number is in the correct position relative to all the other
    # numbers in the array
    # rightIdx at this point is the index of the newly positioned pivot number

    # start with the smaller subarray
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)

    if leftSubarrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


# array = [8, 5, 2, 9, 5, 6, 3]
# print(quickSort(array))
# [2, 3, 5, 5, 6, 8, 9]

"""
12. Merge Sort: 

A divide and conquere algorithm

Solution 1: Create copies of arrays to sort 

Key idea: 
Keep dividing array until get to 1 element arrays and 
merge them into sorted arrays until the entire array is sorted.

Time Complexity:
O(n log n) time: Each level takes O(n) time, and we have O(log n) levels because 
we continuously divide the arrays in half

O(n log n) space

Solution 2: Sort in place

"""


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


# array = [2, 3, 5, 5, 6, 8, 9]
# print(mergeSort(array))


"""

13. Longest palindrome

"""


def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        currentLongest = max(longest, currentLongest, key=lambda x: x[1] - x[0])
    return string[currentLongest[0] : currentLongest[1]]


def getLongestPalindromeFrom(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    return [leftIdx + 1, rightIdx]


"""
14. Invert Binary Tree

For all non-leaf nodes, swap the left and right children nodes

                1
        2               3
    4       5       6       7


                1
        3               2
    5       4       7       6

O(n) time: traverse all the nodes
O(d) or O(log n) space: d is depth (height) of the tree O(d) = O(log n) 
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current is None:
                continue
            array.append(current.value)
            queue.append(current.left)
            queue.append(current.right)
        return array


def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left


n1 = BinaryTree(1)
n2 = BinaryTree(2)
n3 = BinaryTree(3)
n4 = BinaryTree(4)
n5 = BinaryTree(5)
n6 = BinaryTree(6)
n7 = BinaryTree(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
array1 = []
print(n1.breadthFirstSearch(array1))
invertBinaryTree(n1)
array2 = []
print(n1.breadthFirstSearch(array2))

"""
15. Number of Ways to Traverse a Graph

Problem: Given width and height of a rectangular graph, find the number of ways to traverse graph from top left corner to 
bottom right corner

Dynamic Programming
    Dynamic programming: Break a problem down into subproblems. 
                         Solve the subproblems and store the solutions (memoization) to be used to solve the overall problem.

    Key idea: use counts at left and top squares adjacent to current square

For each width index, traverse the height of the graph. 

O(n * m) time: col x row
O(n * m) space: col x row
"""


def numberOfWaysToTraverseGraph(width, height):
    numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
    for widthIdx in range(1, width + 1):
        for heightIdx in range(1, height + 1):
            if widthIdx == 1 or heightIdx == 1:
                numberOfWays[heightIdx][widthIdx] = 1
            else:
                waysLeft = numberOfWays[heightIdx][widthIdx - 1]
                waysUp = numberOfWays[heightIdx - 1][widthIdx]
                numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
    return numberOfWays[height][width]


print(numberOfWaysToTraverseGraph(3, 3))

"""
16. Cycle in Graph

Problem: Given a list of edges, write a function to find if the graph contains a cycle

Key Concept: If visited and currently in stack (can still connect to a next node), then is a cycle

O(v + e) time
O(v) space

"""


def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue

        containsCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if containsCycle:
            return True

    return False


def isNodeInCycle(node, edges, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbors = edges[node]

    for neighbor in neighbors:
        if not visited[neighbor]:
            containsCycle = isNodeInCycle(neighbor, edges, visited, currentlyInStack)
            if containsCycle:
                return True

        elif currentlyInStack[neighbor]:
            return True

    currentlyInStack[node] = False
