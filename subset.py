class Subset:
    def __init__(self, vals):
        self.components = []
        for val in vals:
            self.components.append(val)

    def __str__(self):
        text = "| "
        for val in self.components:
            text = text + str(val) + " - "
        return text[:len(text) - 3] + " |"

    def __hash__(self):
        return hash(str(self.components))

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

    def add(self, singlet):
        if self.is_empty():
            self.components.remove(0)
        self.components.append(singlet)

    def get_components(self):
        return self.components

    def is_empty(self):
        return len(self.components) == 1 and self.components[0] == 0

    def get_size(self):
        return len(self.components)

    def is_inside(self, component: int):
        return self.components.__contains__(component)
