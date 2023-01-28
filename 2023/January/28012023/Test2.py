list = []
for i in range(4):
    list = [(i & 2) >> 1, i & 1]
    print(list, end="")
