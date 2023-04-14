class A:
    def __init__(self):
        print("Class A")


class B:
    # def __init__(self):
    #     print("Class B")
    pass


class C(B, A):
    pass


c = C()
