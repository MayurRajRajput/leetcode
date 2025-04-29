# Design HashSet
""" 
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
from collections import defaultdict
class MyHashSet:
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]

    def add(self, key: int) -> None:
        idx = key % self.n
        if key not in self.arr[idx]:
            self.arr[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.n
        if key in self.arr[idx]:
            self.arr[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % self.n
        return key in self.arr[idx]

commands = ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
values = [[], [1], [2], [1], [3], [2], [2], [2], [2]]
res = []
obj = None
for command,val in zip(commands,values):
    if command == "MyHashSet":
        obj = MyHashSet()
        res.append(None)
    elif command == "add":
        obj.add(val[0])
        res.append(None)
    elif command == "remove":
        obj.remove(val[0])
        res.append(None)
    elif command == "contains":
        result = obj.contains(val[0])
        res.append(result)
print(res)
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
""" 
Example 1:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
 
"""
