from transpose import transpose2d


def test_transpose2d():
    test_cases = [
        ([[-1, 2.0, 3.5], [4.7, 5.0, 6.9]], [[-1.0, 4.7], [2.0, 5.0], [3.5, 6.9]]),
        ([[17.0, 22.0, 3.55], [45.7, 5.0, 6.69]], [[17.0, 45.7], [22.0, 5.0], [3.55, 6.69]]),
        ([[10.0, 20.0, 3.5], [4.7, 50.0, 60.9]], [[10.0, 4.7], [20.0, 50.0], [3.5, 60.9]])
    ]

    for input_matrix, expected_output in test_cases:
        assert transpose2d(input_matrix) == expected_output

