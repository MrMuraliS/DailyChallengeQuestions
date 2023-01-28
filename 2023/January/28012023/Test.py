param = 0
for i in range(4):
    if param == 0:
        list = []
        list.append(0)
        list.append(0)
    elif param == 1:
        list = []
        list.append(0)
        list.append(1)
    elif param == 2:
        list = []
        list.append(1)
        list.append(0)
    elif param == 3:
        list = []
        list.append(1)
        list.append(1)
    param += 1
    print(list, end="")
