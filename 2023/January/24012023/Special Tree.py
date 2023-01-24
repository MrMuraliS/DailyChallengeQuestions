# You are tasked to implement a special tree data structure where the parent node must always be larger in value than all of its children notes
#


class SpecialTree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        if value > self.value:
            self.children.append(SpecialTree(value))
        else:
            print("Value must be larger than parent node")

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value) + ""

        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def __repr__(self):
        return "<tree node representation>"

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, index):
        return self.children[index]

    def __len__(self):
        return len(self.children)

    def __contains__(self, value):
        return value in self.children
