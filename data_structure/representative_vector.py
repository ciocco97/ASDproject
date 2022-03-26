class RepresentativeVector:
    X_VAL = -1

    def __init__(self, size):
        self.vector = [0] * size

    def __str__(self) -> str:
        return ' '.join(map(str, self.vector))

    def set_val_by_index(self, n_i_index, val):
        self.vector[n_i_index] = val

    def get_values(self):
        return self.vector


# this procedure generate the new rv starting from a couple
def generate_new_rv(rv1: RepresentativeVector, rv2: RepresentativeVector, num_of_sets: int) -> RepresentativeVector:
    new = RepresentativeVector(num_of_sets)
    for i, phi1 in enumerate(rv1.get_values()):
        phi2 = rv2.get_values()[i]
        result = phi1 + phi2
        new.set_val_by_index(i, result if 0 <= result <= max(phi1, phi2) else RepresentativeVector.X_VAL)
    return new
