class MyClass:
    def __init__(self):
        self.a = 5
        self.b = 10
        self._dict = {"Name": "John", "Age": 36}

    def add(self):
        print(self["Name"])

    def __getitem__(self, key):
        return self._dict[key]


obj = MyClass()
obj.add()
