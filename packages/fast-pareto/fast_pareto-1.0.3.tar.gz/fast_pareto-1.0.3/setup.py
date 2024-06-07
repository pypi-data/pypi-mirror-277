import sys
import setuptools

from pybind11.setup_helpers import Pybind11Extension
from pybind11.setup_helpers import build_ext


requirements = []
with open("requirements.txt", "r") as f:
    for line in f:
        requirements.append(line.strip())

source_files = ["cpp/hv.cpp", "cpp/hv_wrapper.cpp"]
ext_modules = [Pybind11Extension("fast_pareto_cpp", source_files)]

setuptools.setup(
    name="fast_pareto",
    version="1.0.3",
    author="nabenabe0928",
    author_email="shuhei.watanabe.utokyo@gmail.com",
    url="https://github.com/nabenabe0928/fast-pareto",
    ext_modules=ext_modules,
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    platforms=["Linux"],
    install_requires=requirements,
    cmdclass={"build_ext": build_ext},
)
