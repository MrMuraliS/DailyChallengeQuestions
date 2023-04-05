import queue

# print(help(queue.Queue))

qu = queue.Queue(2)
qu.put(1)
qu.put(2)
qu.put(3)
print(qu.get())
print(qu.get())
