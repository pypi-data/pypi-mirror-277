import numpy as np

from convolution import convolution2d


def test_convolution2d():
    test_cases = [
        # Case with stride 1
        {
            "input_matrix": np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]]),
            "kernel": np.array([[0, 1], [2, 3]]),
            "stride": 1,
            "expected": np.array([[19, 25], [37, 43]])
        },
        # Case with stride 2
        {
            "input_matrix": np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]),
            "kernel": np.array([[1, 0], [0, 1]]),
            "stride": 2,
            "expected": np.array([[7, 11], [23, 27]])
        },
    ]

    for case in test_cases:
        input_matrix = case["input_matrix"]
        kernel = case["kernel"]
        stride = case["stride"]
        expected = case["expected"]

        result = convolution2d(input_matrix, kernel, stride)
        assert np.array_equal(result, expected)
