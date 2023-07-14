import unittest 
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def setUp(self):
        self.heap = MinHeap([10, 15, 20, 17])

    def test_build_heap(self):
        heap2 = MinHeap([30, 20, 15, 5, 10, 12, 6, 40])
        self.assertEqual(heap2.heap, [5, 10, 6, 20, 30, 12, 15, 40])

        heap3 = MinHeap([3, 5, 2, 4, 1])
        self.assertEqual(heap3.heap, [1, 3, 2, 4, 5])

    def test_add(self):
        self.heap.add(9)
        self.assertEqual(self.heap.heap, [9, 10, 20, 17, 15])

    def test_poll(self):
        root = self.heap.poll()
        self.assertEqual(root, 10)
        self.assertEqual(self.heap.heap, [15, 17, 20])

    def test_peek(self):
        self.assertEqual(self.heap.peek(), 10)

if __name__ == '__main__':
    unittest.main()
