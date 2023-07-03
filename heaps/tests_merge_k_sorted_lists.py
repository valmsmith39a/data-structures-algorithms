import unittest
from merge_k_sorted_lists import MergeKSortedLists, ListNode

class MergeKSortedListsTest(unittest.TestCase):

    def setUp(self):
        self.mksl = MergeKSortedLists()

    def test_merge_k_sorted_lists(self):
        lists = [[1,4,5],[1,3,4],[2,6]]
        lists =  [self.list_to_linked_list(nums) for nums in lists]
        merged_head = self.mksl.merge_k_lists(lists)
        self.assertEquals(self.linked_list_to_list(merged_head), [1,1,2,3,4,4,5,6])    
    
    def linked_list_to_list(self, node):
        nums = []
        while node:
            nums.append(node.val)
            node = node.next
        return nums

    def list_to_linked_list(self, nums):
        dummy = ListNode(0)
        current_node = dummy
        for num in nums:
            current_node.next = ListNode(num)
            current_node = current_node.next
        return dummy.next

if __name__ == '__main__':
    unittest.main()
