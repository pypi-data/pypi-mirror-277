from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = cythonize([
    Extension("audiopython.analysis", ["audiopython/analysis.py"]),
    Extension("audiopython.granulator", ["audiopython/granulator.py"]),
    Extension("audiopython.operations", ["audiopython/operations.py"]),
    Extension("audiopython.sampler", ["audiopython/sampler.py"]),
])

setup(
    name="audiopython", 
    version="0.0.6", 
    packages=["audiopython"], 
    ext_modules=extensions, 
    include_dirs=[np.get_include()], 
    install_requires=["numpy"]
)
