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






