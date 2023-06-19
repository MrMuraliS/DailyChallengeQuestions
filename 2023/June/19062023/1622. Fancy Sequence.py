# 1622. Fancy Sequence

"""
Implement the class Fancy which supports the following operations:

- add(val) : Append an integer val to the end of the sequence.
- multAll(m) : Multiply all the values in the sequence by an integer m.
- getIndex(idx) : Gets the current value at index idx (0-indexed) of the sequence modulo 109 + 7. If the index is greater or equal than the length of the sequence, return -1.


Example 1:
    Input
        ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
        [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
    Output
        [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
    Explanation
        Fancy fancy = new Fancy();
        fancy.append(2);   // fancy sequence: [2]
        fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
        fancy.append(7);   // fancy sequence: [5, 7]
        fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
        fancy.getIndex(0); // return 10
        fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
        fancy.append(10);  // fancy sequence: [13, 17, 10]
        fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
        fancy.getIndex(0); // return 26
        fancy.getIndex(1); // return 34
        fancy.getIndex(2); // return 20

Constraints:
    - 1 <= val, m <= 100
    - 0 <= idx <= 105
    - At most 105 calls total will be made to add, multAll, and getIndex.

"""

p = 10**9 + 7
inv = [None] + [pow(m, -1, p) for m in range(1, 101)]


class Fancy:
    def __init__(self):
        self.x = []
        self.a = 1
        self.ainv = 1
        self.b = 0

    def append(self, val):
        self.x.append((val - self.b) * self.ainv)

    def addAll(self, inc):
        self.b += inc

    def multAll(self, m):
        self.a = self.a * m % p
        self.ainv = self.ainv * inv[m] % p
        self.b = self.b * m % p

    def getIndex(self, idx):
        if idx >= len(self.x):
            return -1
        return (self.a * self.x[idx] + self.b) % p


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

# Your Fancy object will be instantiated and called as such:
obj = Fancy()
# obj.append(val)
obj.addAll(inc)
obj.multAll(m)
param_4 = obj.getIndex(idx)
