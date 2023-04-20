import time, sys

import numpy as np
import dask
import dask.array as da

from algorithms.v1 import psort



if __name__ == '__main__':
    dask.config.set(scheduler='threads')
    # dask.config.set(scheduler='processes')
    # dask.config.set(scheduler='synchronous')
    N = eval(sys.argv[1])
    print(N)
    tasks_per_core = 1
    x = da.arange(N, chunks=N/(8*tasks_per_core))[::-1]
    x = psort(x)
    s = time.perf_counter()
    x.compute()
    print(f'Dask: {1000*(time.perf_counter() - s):.4f} ms')

    x = np.arange(N)[::-1]
    s = time.perf_counter()
    np.sort(x)
    print(f'Numpy: {1000*(time.perf_counter() - s):.4f} ms')