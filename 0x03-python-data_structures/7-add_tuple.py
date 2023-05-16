#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = unpack_tuple(tuple_a)
    b1, b2 = unpack_tuple(tuple_b)

    new_tuple = (a1 + b1, a2 + b2)

    return new_tuple


def unpack_tuple(tuple_):
    if len(tuple_) == 0:
        return 0, 0
    elif len(tuple_) == 1:
        return tuple_[0], 0
    else:
        return tuple_[0], tuple_[1]
