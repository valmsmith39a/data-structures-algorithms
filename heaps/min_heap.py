
class MinHeap:
    """
    Implementation of Min Heap 

    A binary heap is a complete binary tree (all levels, possibly except the last, are filled and nodes are as far left as possible).

    A min heap is a type of binary heap where the key (e.g. priority level, timestamp etc) at the root must be the minimum among all the keys in the heap. 

    Each node must be smaller than 2 children nodes. 

    The smallest element in a mean heap is always at the root.
    """

    def __init__(self, data=None):
        if data is None:
            self.heap = [] 
        else:
            self.heap = data
            self.build_heap()

    # O(n) time (not O(n log n)): Average height of nodes on which we call sift_down is less than log n because 
    # there are more nodes at the bottom of the tree than at greater heights 
    # O(1) space: Heapifies the array in place
    def build_heap(self):
        start = self._get_parent_idx(self._get_size() - 1)
        for i in range(start, -1, -1):
            self.sift_down(i)

    # O(log n) time | O(log n space)
    def sift_down(self, idx):
        if self._has_left_child(idx):
            smallest_child_idx = self._get_left_child_idx(idx)
            if (
                self._has_right_child(idx) and
                self.heap[self._get_right_child_idx(idx)] < self.heap[self._get_left_child_idx(idx)]
            ):
                smallest_child_idx = self._get_right_child_idx(idx)
            if (self.heap[idx] > self.heap[smallest_child_idx]):
                self._swap(idx, smallest_child_idx)
                self.sift_down(smallest_child_idx)
            else:
                return 

    # O(log n) time | O(log n) space
    def sift_up(self, idx):
        if (
            self._has_parent(idx) and 
            self.heap[idx] < self.heap[self._get_parent_idx(idx)]
        ):
            self._swap(idx, self._get_parent_idx(idx))
            self.sift_up(self._get_parent_idx(idx))

    # O(log n) time | O(1) space
    def add(self, value):
        self.heap.append(value)
        self.sift_up(self._get_size() - 1)

    # O(log n) time | O(1) space
    def poll(self):
        if self._get_size() == 0:
            return None 
        root = self.heap[0]
        self._swap(0, self._get_size() - 1)
        self.heap.pop()
        self.sift_down(0)
        return root

    # O(1) time | O(1) space
    def peek(self):
        if self._get_size() == 0:
            return None 
        return self.heap[0]
    
    def _get_left_child_idx(self, parent_idx):
        return 2 * parent_idx + 1
    
    def _get_right_child_idx(self, parent_idx):
        return 2 * parent_idx + 2

    def _get_parent_idx(self, child_idx):
        return (child_idx - 1) // 2

    def _has_left_child(self, parent_idx):
        return self._get_left_child_idx(parent_idx) < self._get_size()

    def _has_right_child(self, parent_idx):
        return self._get_right_child_idx(parent_idx) < self._get_size()

    def _has_parent(self, child_idx):
        return self._get_parent_idx(child_idx) >= 0
    
    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def _get_size(self):
        return len(self.heap)
    