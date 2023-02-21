class MyClass:
    def outer(self):
        def inner():
            print("inner")
            self.another()

        print("HEY")
        inner()

    def another(self):
        print("Another")


obj = MyClass()
obj.outer()
