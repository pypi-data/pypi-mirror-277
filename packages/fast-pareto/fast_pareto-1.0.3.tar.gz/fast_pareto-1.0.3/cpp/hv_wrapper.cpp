#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "hv.hpp"

namespace py = pybind11;

PYBIND11_MODULE(fast_pareto_cpp, m) {
    m.def("is_pareto_front_cpp", &is_pareto_front, "A function computing Pareto front");
    m.def("compute_hypervolume_cpp", &compute_hypervolume, "A function computing hypervolume");
}
