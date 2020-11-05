def vector_absolute(vector):
    vector_length = (vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2) ** 0.5
    return vector_length


def cross(vec_a, vec_b):
    cross_x = vec_a[1] * vec_b[2] - vec_a[2] * vec_b[1]
    cross_y = (vec_a[0] * vec_b[2] - vec_a[2] * vec_b[0]) * (-1)
    cross_z = vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0]
    cross_ab = (cross_x, cross_y, cross_z)

    return cross_ab


def unit_vec(vector, length):
    unit_vector = (vector[0]/length, vector[1]/length, vector[2]/length)
    return unit_vector


def dot(vec_a, vec_b):
    product = vec_a[0]*vec_b[0] + vec_a[1]*vec_b[1] + vec_a[2]*vec_b[2]
    return product

