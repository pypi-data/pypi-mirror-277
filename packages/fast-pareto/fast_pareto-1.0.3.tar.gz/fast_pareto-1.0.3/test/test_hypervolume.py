import numpy as np
import pytest

from fast_pareto.hypervolume import hypervolume


def test_hypervolume_2d() -> None:
    for n in range(2, 30):
        r = n * np.ones(2)
        s = np.asarray([[n - 1 - i, i] for i in range(n)])
        for i in range(n + 1):
            s = np.vstack((s, np.asarray([i, n - i])))
        np.random.shuffle(s)
        v = hypervolume(s, r)
        assert v == n * n - n * (n - 1) // 2


def test_hypervolume_3d() -> None:
    n = 3
    r = 10 * np.ones(n)
    s = [np.hstack((np.zeros(i), [1], np.zeros(n - i - 1))) for i in range(n)]
    for _ in range(10):
        s.append(np.random.randint(1, 10, size=(n,)))
    o = np.asarray(s)
    np.random.shuffle(o)
    v = hypervolume(o, r)
    assert v == 10**n - 1


def test_hypervolume_nd() -> None:
    for n in range(2, 10):
        r = 10 * np.ones(n)
        s = [np.hstack((np.zeros(i), [1], np.zeros(n - i - 1))) for i in range(n)]
        for _ in range(10):
            s.append(np.random.randint(1, 10, size=(n,)))
        o = np.asarray(s)
        np.random.shuffle(o)
        v = hypervolume(o, r)
        assert v == 10**n - 1


def test_hypervolume_duplicate_points() -> None:
    n = 3
    r = 10 * np.ones(n)
    s = [np.hstack((np.zeros(i), [1], np.zeros(n - i - 1))) for i in range(n)]
    for _ in range(10):
        s.append(np.random.randint(1, 10, size=(n,)))
    o = np.asarray(s)
    v = hypervolume(o, r)

    # Add an already existing point.
    o = np.vstack([o, o[-1]])

    np.random.shuffle(o)
    v_with_duplicate_point = hypervolume(o, r)
    assert v == v_with_duplicate_point


def test_invalid_input() -> None:
    r = np.ones(3)
    s = np.atleast_2d(2 * np.ones(3))
    with pytest.raises(ValueError):
        _ = hypervolume(s, r)
