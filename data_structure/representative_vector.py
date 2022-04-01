class RepresentativeVector:
    X_VAL = -1

    def __init__(self, components):
        self.vector = components

    def __str__(self) -> str:
        return ' '.join(map(str, self.vector))

    def set_values(self, vals):
        self.vector = vals

    def get_values(self):
        return self.vector


# this procedure generate the new rv starting from a couple
def generate_new_rv(rv1: RepresentativeVector, rv2: RepresentativeVector, N: int) -> RepresentativeVector:
    values = [0]*N
    i = 0
    for phi1, phi2 in zip(rv1.vector, rv2.vector):
        if phi1 or phi2:
            result = phi1 + phi2
            values[i] = result if 0 <= result <= max(phi1, phi2) else RepresentativeVector.X_VAL
        i += 1
    return RepresentativeVector(values)

# this procedure generate the new rv starting from a couple
# def generate_new_rv(rv1: RepresentativeVector, rv2: RepresentativeVector) -> RepresentativeVector:
#     values = []
#     for phi1, phi2 in zip(rv1.vector, rv2.vector):
#         result = phi1 + phi2
#         values.append(result if 0 <= result <= max(phi1, phi2) else RepresentativeVector.X_VAL)
#     return RepresentativeVector(values)
