from __future__ import annotations

import numpy as np

from fast_pareto.pareto import _change_directions
from fast_pareto.pareto import is_pareto_front

from sortedcontainers import SortedList


def _compute_exclusive_hv(limited_sols: np.ndarray, inclusive_hv: float, ref_point: np.ndarray) -> float:
    if limited_sols.shape[0] == 0:
        return inclusive_hv

    on_front = is_pareto_front(limited_sols)
    return inclusive_hv - _hypervolume_nd(limited_sols[on_front], ref_point)


def _hypervolume_nd(costs: np.ndarray, ref_point: np.ndarray) -> float:
    inclusive_hvs = np.prod(ref_point - costs, axis=-1)
    if inclusive_hvs.shape[0] == 1:
        return float(inclusive_hvs[0])
    elif inclusive_hvs.shape[0] == 2:
        # S(A v B) = S(A) + S(B) - S(A ^ B).
        intersec = np.prod(ref_point - np.maximum(costs[0], costs[1]))
        return np.sum(inclusive_hvs) - intersec

    limited_sols_array = np.maximum(costs[:, np.newaxis], costs)
    return sum(
        _compute_exclusive_hv(limited_sols_array[i, i + 1 :], inclusive_hv, ref_point)  # NOQA: E203
        for i, inclusive_hv in enumerate(inclusive_hvs)
    )


def _hypervolume_2d(costs: np.ndarray, ref_point: np.ndarray) -> float:
    assert costs.shape[1] == 2 and ref_point.shape[0] == 2
    rect_diag_y = np.append(ref_point[1], costs[:-1, 1])
    edge_length_x = ref_point[0] - costs[:, 0]
    edge_length_y = rect_diag_y - costs[:, 1]
    return edge_length_x @ edge_length_y


def _hypervolume_3d(costs: np.ndarray, ref_point: np.ndarray) -> float:
    hv = 0.0
    # NOTE(nabenabe0928): The indices of Y and Z in the sorted lists are the reverse of each other.
    nondominated_Y = SortedList([-float("inf"), ref_point[1]])
    nondominated_Z = SortedList([-float("inf"), ref_point[2]])
    for cost in costs:
        n_nondominated = len(nondominated_Y)
        # nondominated_Y[left - 1] < y <= nondominated_Y[left]
        left = nondominated_Y.bisect_left(cost[1])
        # nondominated_Z[- right - 1] < z <= nondominated_Z[-right]
        right = n_nondominated - nondominated_Z.bisect_left(cost[2])
        assert 0 < left <= right < n_nondominated
        diagonal_point = np.asarray([nondominated_Y[right], nondominated_Z[-left]])
        inclusive_hv = np.prod(diagonal_point - cost[1:])
        dominated_sols = np.stack([nondominated_Y[left:right], list(reversed(nondominated_Z[-right:-left]))], axis=-1)
        del nondominated_Y[left:right]
        del nondominated_Z[-right:-left]
        nondominated_Y.add(cost[1])
        nondominated_Z.add(cost[2])
        hv += (inclusive_hv - _hypervolume_2d(dominated_sols, diagonal_point)) * (ref_point[0] - cost[0])

    return hv


def hypervolume(
    costs: np.ndarray,
    ref_point: np.ndarray,
    larger_is_better_objectives: list[int] | None = None,
    assume_pareto: bool = False,
) -> float:
    """
    Calculate the hypervolume of the given costs.

    Args:
        costs (np.ndarray):
            An array of costs (or objectives).
            The shape is (n_observations, n_objectives).
        ref_point (np.ndarray):
            The reference point for the hypervolume calculation.
            This point must be worse than all the point in costs.
        larger_is_better_objectives (list[int] | None):
            The indices of the objectives that are better when the values are larger.
            If None, we consider all objectives are better when they are smaller.
        assume_pareto (bool):
            Whether to assume that costs is a Pareto set.

    Returns:
        hypervolume (float):
            Hypervolume of the given costs and ref_point.
    """
    _costs = _change_directions(costs, larger_is_better_objectives)
    _ref_point = _change_directions(ref_point[np.newaxis, :], larger_is_better_objectives)[0]
    if np.any(_ref_point < _costs):
        raise ValueError("All values in costs must be better than ref_point.")

    if not assume_pareto:
        _costs = _costs[is_pareto_front(_costs)]

    if not np.all(np.isfinite(ref_point)):
        return float("inf")

    # _costs is now unique-lexsorted Pareto solutions.
    _costs = np.unique(_costs, axis=0)
    if ref_point.shape[0] == 2:
        return _hypervolume_2d(_costs, ref_point)
    elif ref_point.shape[0] == 3:
        return _hypervolume_3d(_costs, ref_point)

    return _hypervolume_nd(_costs, ref_point)
