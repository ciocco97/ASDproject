import copy


class Subset:
    def __init__(self, vals):
        self.components = copy.deepcopy(vals)

    def __str__(self):
        text = ""
        for val in self.components:
            text = text + str(val) + " - "
        return text.removesuffix(" - ")

    def compare(self, other):
        if isinstance(other, Subset):
            for i, val in enumerate(self.components):
                oval = other.components[i]
                if val < oval:
                    return -1
                elif val > oval:
                    return 1
            return 0

    def max(self):
        return max(self.components)
