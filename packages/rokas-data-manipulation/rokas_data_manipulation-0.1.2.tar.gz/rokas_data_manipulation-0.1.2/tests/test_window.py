import numpy as np
from window import window1d


def test_window1d():
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, 2, 1, [[1, 2, 3], [3, 4, 5], [5, 6, 7]]),
        (np.array([1, 2, 3, 4, 5, 6, 7]), 3, 1, 1,
         [np.array([1, 2, 3]), np.array([2, 3, 4]), np.array([3, 4, 5]), np.array([4, 5, 6]), np.array([5, 6, 7])]),
        ([1, 2, 3, 4, 5, 6, 7], 2, 2, 1, [[1, 2], [3, 4], [5, 6]]),
        ([1, 2, 3, 4, 5, 6, 7], 2, 1, 2, [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]),
        ([1, 2, 3, 4, 5], 3, 1, 1, [[1, 2, 3], [2, 3, 4], [3, 4, 5]]),
        ([1, 2], 3, 1, 1, [])
    ]

    for input_array, size, shift, stride, expected_output in test_cases:
        result = window1d(input_array, size, shift, stride)
        for res, exp in zip(result, expected_output):
            assert np.array_equal(res, exp)
