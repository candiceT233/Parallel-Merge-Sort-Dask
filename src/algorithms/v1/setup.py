from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='merge module',
    ext_modules=cythonize('merge.pyx')
)