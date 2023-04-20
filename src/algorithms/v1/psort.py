import numpy as np

from .merge import merge_c


def merge_chunks(chunks):
    if len(chunks) == 1:
        return tuple()
    return tuple(chunks[i] + chunks[i+1] for i in range(0, len(chunks)-1, 2))


def psort(x):
    chunks = x.chunks[0]
    x = x.map_blocks(np.sort)
    while len(chunks) >= 2:
#         print(x.compute())
        chunks = merge_chunks(chunks)
        x = x.rechunk((chunks,))
        x = x.map_blocks(merge_c, dtype=int)
    return x