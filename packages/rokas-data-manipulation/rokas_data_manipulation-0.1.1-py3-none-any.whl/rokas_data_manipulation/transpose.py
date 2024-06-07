
def transpose2d(input_matrix: list[list[float]]) -> list[list[float]]:
    """
    Transposes a 2D matrix.

    Args:
    input_matrix (list[list[float]]): Input 2D matrix.

    Returns:
    list[list[float]]: Transposed matrix.
    """
    # Validate input types and values
    if not (isinstance(input_matrix, list) and all(isinstance(row, list) for row in input_matrix)):
        raise ValueError("Input must be a list of lists")
    if not all(isinstance(item, (int, float)) for row in input_matrix for item in row):
        raise ValueError("All items in the matrix must be numbers")
    if len(input_matrix) == 0 or any(len(row) != len(input_matrix[0]) for row in input_matrix):
        raise ValueError("All rows must have the same number of elements")

    return [list(row) for row in zip(*input_matrix)]
