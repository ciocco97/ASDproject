import collections
import copy
import hashlib


class Subset:
    def __init__(self, vals):
        self.components = vals.copy()

    def __str__(self):
        text = ""
        for val in self.components:
            text = text + str(val) + ","
        return text[:len(text) - 1]

    def __hash__(self):
        return hash(str(self.components))

    def max(self):
        return max(self.components)

    def add(self, singlet):
        if len(self.components) == 1 and self.components[0] == 0:
            self.components.remove(0)
        self.components.append(singlet)

    def pop_right(self):
        if len(self.components) == 0:
            self.components.append(0)
        self.components.pop()

    def get_components(self):
        return self.components

    def get_size(self):
        return len(self.components)
