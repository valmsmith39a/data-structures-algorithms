# class Node:
#     def __init__(self, name):
#         self.name = name
#         self.children = []

#     def depthFirstSearch(self, array):
#         array.append(self.name)
#         for child in self.children:
#             child.depthFirstSearch(array)
#         return array


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

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def height(node):
#     if node is None:
#         return 0
#     return 1 + max(height(node.left), height(node.right))

# n0 = BinaryTree(0)
# n1 = BinaryTree(1)
# n2 = BinaryTree(2)
# n3 = BinaryTree(3)
# n4 = BinaryTree(4)
# n0.left = n1
# n0.right = n2
# n1.left = n3
# n1.right = n4
#  # 3
# print(height(n0))


# def quickSort(array, startIdx, endIdx):
#     if startIdx >= endIdx:
#         return array
#     pivotIdx = startIdx
#     leftIdx = startIdx + 1
#     rightIdx = endIdx

#     while rightIdx >= leftIdx:
#         if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
#             swap(array, leftIdx, rightIdx)
#         if array[leftIdx] <= array[pivotIdx]:
#             leftIdx += 1
#         if array[rightIdx] >= array[pivotIdx]:
#             rightIdx -= 1
#     swap(array, pivotIdx, rightIdx)

#     leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
#     if leftSubarrayIsSmaller:
#         quickSort(array, startIdx, rightIdx - 1)
#         quickSort(array, rightIdx + 1, endIdx)
#     else:
#         quickSort(array, rightIdx + 1, endIdx)
#         quickSort(array, startIdx, rightIdx - 1)


# def swap(array, i, j):
#     array[i], array[j] = array[j], array[i]


# array = [8, 5, 2, 9, 5, 6, 3]
# print(array)
# quickSort(array, 0, 6)
# print(array)


# def mergeSort(array):
#     if len(array) == 1:
#         return array
#     middleIdx = len(array) // 2  # floor
#     leftHalf = array[:middleIdx]
#     rightHalf = array[middleIdx:]
#     return mergeSortedArray(mergeSort(leftHalf), mergeSort(rightHalf))


# def mergeSortedArray(leftHalf, rightHalf):
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     i = j = k = 0

#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] < rightHalf[j]:
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1

#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1

#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1

#     return sortedArray


# array = [8, 5, 2, 9, 5, 6, 3]
# print("initial array ", array)
# print("merge sort result", mergeSort(array))


# def numberOfWaysToTraverseGraph(width, height):
#     numberOfWays = [[0 for _ in range(width + 1)] for _ in range(height + 1)]
#     for widthIdx in range(1, width + 1):
#         for heightIdx in range(1, height + 1):
#             if widthIdx == 1 or heightIdx == 1:
#                 numberOfWays[heightIdx][widthIdx] = 1
#             else:
#                 waysLeft = numberOfWays[heightIdx][widthIdx - 1]
#                 waysUp = numberOfWays[heightIdx - 1][widthIdx]
#                 numberOfWays[heightIdx][widthIdx] = waysLeft + waysUp
#     return numberOfWays[height][width]


# print(numberOfWaysToTraverseGraph(3, 3))
# 6


def cycleInGraph(edges):
    numberOfNodes = len(edges)
    visited = [False for _ in range(numberOfNodes)]
    currentlyInStack = [False for _ in range(numberOfNodes)]

    for node in range(numberOfNodes):
        if visited[node]:
            continue
        isNodeContainedInCycle = isNodeInCycle(node, edges, visited, currentlyInStack)
        if isNodeContainedInCycle:
            return True
    return False


def isNodeInCycle(node, edges, visited, currentlyInStack):
    visited[node] = True
    currentlyInStack[node] = True

    neighbors = edges[node]

    for neighbor in neighbors:
        if not visited[neighbor]:
            isNeighborContainedInCycle = isNodeInCycle(
                neighbor, edges, visited, currentlyInStack
            )
            if isNeighborContainedInCycle:
                return True
        elif currentlyInStack[neighbor]:
            return True
    currentlyInStack[node] = False
    return False


edges = [[1, 2], [], [3, 4], [], [5], [6], [4]]
print(cycleInGraph(edges))
# True

edges2 = [[1, 2], [], [3, 4], [], [5], [6], []]
print(cycleInGraph(edges2))
# False
