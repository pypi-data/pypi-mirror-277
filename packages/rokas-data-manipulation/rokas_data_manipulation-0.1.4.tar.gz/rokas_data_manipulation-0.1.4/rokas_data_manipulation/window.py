from __future__ import annotations
import numpy as np


def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    """
    Generate time series windows.

    Args:
    input_array (list | np.ndarray): Input 1D array.
    size (int): Size of the window.
    shift (int): Positive integer that determines the shift (step size) between different windows.
    stride (int): Positive integer that determines the stride (step size) within each window.

    Returns:
    list[list | np.ndarray]: List of time series windows.
    """
    # Validate input types and values
    if not isinstance(input_array, (list, np.ndarray)):
        raise TypeError("Input_array must be a list or a NumPy array")
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer")
    if not isinstance(shift, int) or shift <= 0:
        raise ValueError("Shift must be a positive integer")
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError("Stride must be a positive integer")

    # Convert input_array to a NumPy array if it's a list
    if isinstance(input_array, list):
        input_array = np.array(input_array)

    windows = []
    # Generate windows by moving across the input array
    for start in range(0, len(input_array) - (size - 1) * stride, shift):
        # Extract a window from the input array
        window = input_array[start:start + size * stride:stride]
        windows.append(window)

    return windows
