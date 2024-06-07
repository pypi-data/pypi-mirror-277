from __future__ import annotations

from copy import deepcopy
from typing import Literal

import numpy as np

import scipy.stats


def _change_directions(costs: np.ndarray, larger_is_better_objectives: list[int] | None = None) -> np.ndarray:
    """
    Determine the Pareto front from a provided set of costs.

    Args:
        costs (np.ndarray):
            An array of costs (or objectives).
            The shape is (n_observations, n_objectives).
        larger_is_better_objectives (list[int] | None):
            The indices of the objectives that are better when the values are larger.
            If None, we consider all objectives are better when they are smaller.

    Returns:
        transformed_costs (np.ndarray):
            An array of costs (or objectives) that are transformed so that
            smaller is better.
            The shape is (n_observations, n_objectives).
    """
    n_objectives = costs.shape[-1]
    _costs = deepcopy(costs)
    if larger_is_better_objectives is None or len(larger_is_better_objectives) == 0:
        return _costs

    if max(larger_is_better_objectives) >= n_objectives or min(larger_is_better_objectives) < 0:
        raise ValueError(
            "The indices specified in larger_is_better_objectives must be in "
            f"[0, n_objectives(={n_objectives})), but got {larger_is_better_objectives}"
        )

    _costs[..., larger_is_better_objectives] *= -1
    return _costs


def _is_pareto_front_2d(costs: np.ndarray) -> np.ndarray:
    (n_observations, _) = costs.shape
    cummin_value1 = np.minimum.accumulate(costs[:, 1])
    on_front = np.ones(n_observations, dtype=bool)
    on_front[1:] = cummin_value1[1:] < cummin_value1[:-1]  # True if cummin value1 is new minimum.
    return on_front


def _is_pareto_front_nd(costs: np.ndarray) -> np.ndarray:
    (n_observations, _) = costs.shape
    on_front = np.zeros(n_observations, dtype=bool)
    nondominated_indices = np.arange(n_observations)
    while len(costs):
        # The following judges `np.any(costs[i] < costs[0])` for each `i`.
        nondominated_and_not_top = np.any(costs < costs[0], axis=1)
        # NOTE: trials[j] cannot dominate trials[i] for i < j because of lexsort.
        # Therefore, nondominated_indices[0] is always non-dominated.
        on_front[nondominated_indices[0]] = True
        costs = costs[nondominated_and_not_top]
        nondominated_indices = nondominated_indices[nondominated_and_not_top]

    return on_front


def is_pareto_front(
    costs: np.ndarray, larger_is_better_objectives: list[int] | None = None, assume_unique_lexsorted: bool = False
) -> np.ndarray:
    """
    Determine the Pareto front from a provided set of costs.
    The time complexity is O(N (log N)^(M - 2)) for M > 3
    and O(N log N) for M = 2, 3 where
    N is n_observations and M is n_objectives. (Kung's algorithm)

    Args:
        costs (np.ndarray):
            An array of costs (or objectives).
            The shape is (n_observations, n_objectives).
        larger_is_better_objectives (list[int] | None):
            The indices of the objectives that are better when the values are larger.
            If None, we consider all objectives are better when they are smaller.
        assume_unique_lexsorted (bool):
            Whether to assume the unique lexsorted costs or not.
            Basically, we omit np.unique(costs, axis=0) if True.

    Returns:
        on_front (np.ndarray):
            Whether the solution is on the Pareto front.
            Each element is True or False and the shape is (n_observations, ).

    NOTE:
        f dominates g if and only if:
            1. f[i] <= g[i] for all i, and
            2. f[i] < g[i] for some i
        ==> g is not dominated by f if and only if:
            1. f[i] > g[i] for some i, or
            2. f[i] == g[i] for all i

        If we filter all observations by only the condition 1,
        we might miss the observations that satisfy the condition 2.
    """
    _costs = _change_directions(costs, larger_is_better_objectives)
    apply_unique = bool(larger_is_better_objectives is not None or not assume_unique_lexsorted)
    if apply_unique:
        _costs, order_inv = np.unique(_costs, axis=0, return_inverse=True)

    if costs.shape[-1] == 2:
        on_front = _is_pareto_front_2d(_costs)
    else:
        on_front = _is_pareto_front_nd(_costs)

    return on_front[order_inv.flatten()] if apply_unique else on_front


def _compute_rank_based_crowding_distance(ranks: np.ndarray) -> np.ndarray:
    (n_observations, n_obj) = ranks.shape
    order = np.argsort(ranks, axis=0)
    order_inv = np.zeros_like(order[:, 0], dtype=int)
    dists = np.zeros(n_observations)
    for m in range(n_obj):
        sorted_ranks = ranks[:, m][order[:, m]]
        order_inv[order[:, m]] = np.arange(n_observations)
        scale = sorted_ranks[-1] - sorted_ranks[0]
        crowding_dists = np.hstack([np.inf, sorted_ranks[2:] - sorted_ranks[:-2], np.inf]) / scale
        dists += crowding_dists[order_inv]

    # crowding dist is better when it is larger
    return scipy.stats.rankdata(-dists).astype(int)


def _tie_break_by_method(
    nd_masks: list[list[int]], ranks: np.ndarray, avg_ranks: np.ndarray | None = None
) -> np.ndarray:
    """
    Tie-break the non-domination ranks (, but we cannot guarantee no duplications)

    Args:
        nd_masks (list[list[int]]):
            The indices of observations in each non-domination rank.
        ranks (np.ndarray):
            The ranks of each objective in each observation.
            The shape is (n_observations, n_obj).
        avg_ranks (np.ndarray | None):
            The average rank + small deviation by the best rank of objectives in each observation.
            The shape is (n_observations, ).

    Returns:
        tie_broken_nd_ranks (np.ndarray):
            The each non-dominated rank will be tie-broken
            so that we can sort identically (but we may get duplications).
            The shape is (n_observations, ) and the array is a permutation of zero to n_observations - 1.

    Reference for avg_rank:
        Paper Title:
            Techniques for Highly Multiobjective Optimisation: Some Nondominated Points are Better than Others
        One sentence summary:
            Average ranking strategy is effective to tie-break in some evolution strategies methods.
        Authors:
            David Come and Joshua Knowles
        URL:
            https://arxiv.org/pdf/0908.3025.pdf

    Reference for crowding distance:
        Paper Title:
            A fast and elitist multiobjective genetic algorithm: NSGA-II
        One sentence summary:
            Consider the proximity to neighbors.
        Authors:
            K. Deb et al.
        URL:
            http://vision.ucsd.edu/~sagarwal/nsga2.pdf
    """
    n_checked = 0
    (size, _) = ranks.shape
    tie_broken_nd_ranks = np.zeros(size, dtype=int)

    for mask in nd_masks:
        if avg_ranks is not None:
            tie_break_ranks = scipy.stats.rankdata(avg_ranks[mask]).astype(int)
        else:  # Use crowding distance
            tie_break_ranks = _compute_rank_based_crowding_distance(ranks=ranks[mask])

        # -1 to start tie_broken_nd_ranks from zero
        tie_broken_nd_ranks[mask] = tie_break_ranks + n_checked - 1
        n_checked += len(mask)

    return tie_broken_nd_ranks


def _tie_break(
    costs: np.ndarray, nd_ranks: np.ndarray, tie_break: Literal["crowding_distance", "avg_rank"]
) -> np.ndarray:
    methods = ["crowding_distance", "avg_rank"]
    ranks = scipy.stats.rankdata(costs, axis=0)
    masks: list[list[int]] = [[] for _ in range(nd_ranks.max() + 1)]
    for idx, nd_rank in enumerate(nd_ranks):
        masks[nd_rank].append(idx)

    if tie_break == methods[0]:
        return _tie_break_by_method(nd_masks=masks, ranks=ranks)
    elif tie_break == methods[1]:
        # min_ranks_factor plays a role when we tie-break same average ranks
        min_ranks_factor = np.min(ranks, axis=-1) / (nd_ranks.size**2 + 1)
        avg_ranks = np.mean(ranks, axis=-1) + min_ranks_factor
        return _tie_break_by_method(nd_masks=masks, ranks=ranks, avg_ranks=avg_ranks)
    else:
        raise ValueError(f"tie_break method must be in {methods}, but got {tie_break}")


def _nondominated_rank(costs: np.ndarray) -> np.ndarray:
    (n_observations, n_obj) = costs.shape
    if n_obj == 1:
        return np.unique(costs[:, 0], return_inverse=True)[1]

    ranks = np.zeros(n_observations, dtype=int)
    rank = 0
    indices = np.arange(n_observations)
    while indices.size > 0:
        on_front = is_pareto_front(costs, assume_unique_lexsorted=True)
        ranks[indices[on_front]] = rank
        # Remove Pareto front points
        indices, costs = indices[~on_front], costs[~on_front]
        rank += 1

    return ranks


def nondominated_rank(
    costs: np.ndarray,
    larger_is_better_objectives: list[int] | None = None,
    tie_break: Literal["crowding_distance", "avg_rank"] | None = None,
) -> np.ndarray:
    """
    Calculate the non-dominated rank of each observation.

    Args:
        costs (np.ndarray):
            An array of costs (or objectives).
            The shape is (n_observations, n_objectives).
        larger_is_better_objectives (list[int] | None):
            The indices of the objectives that are better when the values are larger.
            If None, we consider all objectives are better when they are smaller.
        tie_break (bool):
            Whether we apply tie-break or not.

    Returns:
        ranks (np.ndarray):
            IF not tie_break:
                The non-dominated rank of each observation.
                The shape is (n_observations, ).
                The rank starts from zero and lower rank is better.
            else:
                The each non-dominated rank will be tie-broken
                so that we can sort identically.
                The shape is (n_observations, ) and the array is a permutation of zero to n_observations - 1.
    """
    (_, n_obj) = costs.shape
    _costs = _change_directions(costs, larger_is_better_objectives)
    cached_costs = _costs.copy()
    _costs, order_inv = np.unique(_costs, axis=0, return_inverse=True)
    ranks = _nondominated_rank(costs=_costs)[order_inv.flatten()]

    if tie_break is None:
        return ranks
    else:
        return _tie_break(cached_costs, ranks, tie_break)
