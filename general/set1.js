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
// console.log('move zeros is: ', moveZeroes(nums))

/*

 Given two strings s and t, write a function to determine if t is an anagram of s.
 Input: s = "anagram", t = "nagaram"
 Output: true

 Input: s = "rat", t = "car"
 Output: false

*/

function anagram (s, t) {
  if (s.length !== t.length) return false
  return s.split('').sort().join('') === t.split('').sort().join('')
}

const s = 'anagram'
const t = 'nagaram'
// const s = 'rat'
// const t = 'car'
console.log(anagram(s, t))