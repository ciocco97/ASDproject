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
        # print(f"Max function: {self.components}")
        return max(self.components)

    def add(self, singoletto):
        self.components.append(singoletto)

    def get_components(self):
        return self.components
