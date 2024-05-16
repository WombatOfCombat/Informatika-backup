import numpy as np

def elements_wise(arr: np.ndarray, f):
    with np.nditer(arr, op_flags=['readwrite']) as it:
        for x in it:
            print(x)
            x[...] = f(x)
    return None

def func(x):
    return x**x + 3*x + 2
a1 = np.array(range(2 * 2 * 3), dtype=float).reshape(2, 2, -1)
a2 = np.array(range(2 * 3), dtype=float).reshape(2, -1)
elements_wise(a1, func)
elements_wise(a2, func)
print(f"a1:\n {a1}")
print(f"a2:\n {a2}")