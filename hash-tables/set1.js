/*
  Given a non-empty array of integers, return the k most frequent elements.
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
*/

function topKFrequent(nums, k) {
  let count = {}
  let sortedCount = []
  let result = []
  for(let i = 0; i < nums.length; i++) {
      const key = nums[i]
      if (count[key]) {
          count[key] = ++count[key]
      } else {
          count[key] = 1
      }
  }
  sortedCount = Object.keys(count).sort((a, b) => count[b] - count[a])
  for (let j = 0; j < k; j++) {
      result.push(sortedCount[j])
  }
  return result
}

console.log('top k frequent: ', topKFrequent([1,1,1,2,2,3], 2))
