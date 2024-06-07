# Data Manipulation

A package for common data manipulation operations in Python.

## Features

- **Transpose 2D Matrix**: Transpose a given 2D matrix.
- **Generate 1D Windows**: Create time series windows from a 1D array.
- **2D Convolution**: Perform 2D cross-correlation.

## Installation

### Prerequisites

- Python 3.9 or higher
- [Poetry](https://python-poetry.org/docs/#installation)

### Setting Up the Project

1. **Clone the repository**:

   ```
   git clone https://github.com/TuringCollegeSubmissions/rgaldi-DE2v2.1.5.git
2. **Install dependencies**:
   ```
   poetry install
3. **Activate the virtual environment**:
   ``` 
   poetry shell

## **Usage**
   ```
   from rokas_data_manipulation import transpose2d, window1d
   
   # Example usage
   matrix = [[1, 2, 3], [4, 5, 6]]
   transposed = transpose2d(matrix)
   print(transposed)
   
   array = [1, 2, 3, 4, 5, 6, 7]
   windows = window1d(array, size=2, shift=2, stride=2)
   print(windows) 
   ```
### **Testing**:
   ```
   poetry run pytest
   ```
