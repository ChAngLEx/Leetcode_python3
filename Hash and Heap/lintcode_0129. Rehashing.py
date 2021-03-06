The size of the hash table is not determinate at the very beginning. If the total size of keys is too large (e.g. size >= capacity / 10), we should double the size of the hash table and rehash every keys. Say you have a hash table looks like below:

size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
The hash function is:

int hashcode(int key, int capacity) {
    return key % capacity;
}
here we have three numbers, 9, 14 and 21, where 21 and 9 share the same position as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
Given the original hash table, return the new hash table after rehashing .

Example

Example 1

Input : [null, 21->9->null, 14->null, null]
Output : [null, 9->null, null, null, null, 21->null, 14->null, null]
Notice

For negative integer in hash table, the position can be calculated as follow:

C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
Python: you can directly use -1 % 3, you will get 2 automatically.
Input test data (one parameter per line)
How to understand a testcase?




思路：
算扩容之后的 size (origin_len * 2)
遍历原来的 hashtable 和每个 listnode
重算在 new_hashtable 的 index
在新的位置已经有 node 就到 tails 里面找 tail 串，否则就初始化 heads[i] 和 tails[i]

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        if not hashTable:
            return []
            
        size = len(hashTable) * 2
        #用于记录hash的key
        new_hash_head = [None] * size
        #用于记录每个hash[key]这一linkedlist的最后一个point
        new_hash_tail = [None] * size
        
        for node in hashTable:
            curt = node
            
            while curt:
                #求的该point在新hash中的index,即key值
                index = curt.val % size
                #新建point
                temp_node = ListNode(curt.val)
                
                #当该index在hash中已经有值了,即这已经存在一个链表,新的point则需要被放在链表的尾部,即tail.next
                if new_hash_head[index]:
                    new_hash_tail[index].next = temp_node
                #当hash[index]为空,即不存在链表时,直接将point放入即可
                else:
                    new_hash_head[index] = temp_node
                
                #更新tail,保证tail[index]一直是该linkedlist的最后一个point
                new_hash_tail[index] = temp_node
                
                curt = curt.next
        
        return new_hash_head
        
                
