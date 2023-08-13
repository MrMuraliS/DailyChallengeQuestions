class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []

    def get(self, index):
        try:
            return self.data[index]
        except:
            return "Undefined"


new_array = MyArray()
print(new_array.get(0))
