cimport cython
import numpy as np


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
def merge_c(int[::1] x):
    out = np.zeros(len(x), dtype=int)
    cdef int[::1] out_view = out
    cdef int mid = (x.shape[0] - 1) // 2 + 1
    cdef int i = 0
    cdef int j = mid
    cdef int k = 0
    while i < mid and j < x.shape[0]:
        if x[i] < x[j]:
            out_view[k] = x[i]
            i += 1
        else:
            out_view[k] = x[j]
            j += 1
        k += 1

    while i < mid:
        out_view[k] = x[i]
        k += 1
        i += 1
    while j < x.shape[0]:
        out_view[k] = x[j]
        k += 1
        j += 1
    return out