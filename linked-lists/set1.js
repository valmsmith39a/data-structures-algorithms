/*
  Linked List:
  * Sequence of nodes
  * Singly linked list: each node points to next node
  * Doubly linked list: each node points to next/previous
  * To get Kth element, need to iterate through K elements
  * Benefit: Add/Remove items from beginning of linked list in constant time
  * 
  * "Runner Technique"
*/

// Creating a linked list
// Basic implementation
/*
class LinkedList {

  constructor (value) {
    this.head = {
      value,
      next: null
    }
    this.length = 1
  }
}

console.log(new LinkedList('Hello!'))
// -> { head: { value: 'Hello!, next: null}}
*/

/* Singly Linked List */

// Singly Linked List: Add to Head
/*
  Linked list is first in first out (FIFO)

 (tail)                                    (head)
  node1               node2                node3
  node1.next = null   node2.next = node1   node2.next = node2  
*/

class LinkedList {
  constructor(value) {
    this.head = null
    this.length = 0
    this.addToHead(value)
  }

  addToHead(value) {
    const newNode = { value }
    newNode.next = this.head
    this.head = newNode
    this.length++
    return this
  }
}

const list = new LinkedList('node1')
console.log('list with 1 node is: ', list)

list.addToHead('node2')
console.log('list with 2 nodes is: ', list)

list.addToHead('node3')
console.log('list with 3 nodes is: ', list)



