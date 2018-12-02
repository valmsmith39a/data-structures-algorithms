
/*
  isUnique: Implement an algorithm to determine if a string has all
  unique characters. What if you cannot use additional data structures?
*/
function isUnique(str) {
  let charSet = []
  if (str.length > 128) {
    return false
  }
  for (let i = 0; i < str.length; i++) {
    const val = str.charAt(i)
    if (charSet[val]) {
      return false
    }
    charSet[val] = true
  }
  return true
}
console.log(isUnique('abc'))
console.log(isUnique('abbc'))
console.log('time complexity: O(min(c, n)) time')
console.log('space complexity: O(1) or O(c) space')

