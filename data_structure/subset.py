import collections
import copy
import hashlib
from array import array


class Subset:
    def __init__(self, vals):
        self.components = vals.copy()

    def __str__(self):
        return str(self.components)

    def max(self):
        # the last component is the highest
        return 0 if len(self.components) == 0 else self.components[len(self.components)-1]

    def add(self, singlet):
        self.components.append(singlet)

    def popright(self):
        self.components.pop()

    def get_components(self):
        return self.components

    def get_size(self):
        return len(self.components)
