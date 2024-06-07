import numpy as np


def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    """
    Perform 2D cross-correlation.

    Args:
    input_matrix (np.ndarray): Input 2D matrix.
    kernel (np.ndarray): 2D kernel matrix.
    stride (int): Positive integer that determines the stride (step size) within each window.

    Returns:
    np.ndarray: Resulting matrix after cross-correlation.
    """
    # Validate input types and values
    if not isinstance(input_matrix, np.ndarray):
        raise ValueError("Input_matrix must be np.ndarray")
    if not isinstance(kernel, np.ndarray):
        raise ValueError("Kernel must be np.ndarray")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("Stride must be a positive integer")

    # Get the shape of the input matrix
    input_height, input_width = input_matrix.shape
    # Get the shape of the kernel matrix
    kernel_height, kernel_width = kernel.shape

    if kernel_height > input_height or kernel_width > input_width:
        raise ValueError("Kernel size must be smaller than or equal to the input_matrix size")

    # Calculate the output dimensions
    # Determines how many positions the kernel can move vertically
    output_height = (input_height - kernel_height) // stride + 1
    # Determines how many positions the kernel can move horizontally
    output_width = (input_width - kernel_width) // stride + 1
    output_matrix = np.zeros((output_height, output_width))

    for x in range(output_height):
        for y in range(output_width):
            # Extract the patch of the input matrix that the kernel is currently on
            patch = input_matrix[x * stride: x * stride + kernel_height, y * stride: y * stride + kernel_width]
            # Perform element-wise multiplication and sum the result to get the output matrix value
            output_matrix[x, y] = np.sum(patch * kernel)

    return output_matrix
