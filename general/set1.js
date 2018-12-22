/*

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

*/

function moveZeroes(nums) {
  let zeroes = []
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      nums.splice(i, 1)
      zeroes.push(0)
      i--
    }
  }
  nums.push.apply(nums, zeroes)
  return nums
}

let nums = [0,1,0,3,12]
// let nums = [0, 0, 1]

console.log('move zeros is: ', moveZeroes(nums))