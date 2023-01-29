"""
how can I rearrange this array
a = [3,5,2,6,8,4,4,6,4,4,3] and x = 5 to this
output array = [3,2,3,4,4,4,4,5,6,8,6]
without using a sorting routine of any kind
"""

# a = [3,5,2,6,8,4,4,6,4,4,3]
# x = 5
# b = []
# c = []
# for i in a:
#     if i < x:
#         b.append(i)
#     else:
#         c.append(i)
# print(b+c)

b = [3, 5, 2, 6, 8, 4, 4, 6, 4, 4, 3]
x = 5
# for item in b:
#     if item < x:
#         b.remove(item)
#         idx = b.index(item)
#         b.insert(idx,item)
# print(b)

i = 0
while i < len(b):
    print(i, b)
    if b[i] > x and b[i + 1] == x:
        b[i], b[i + 1] = b[i + 1], b[i]
        i -= 1
    i += 1
print(b)
