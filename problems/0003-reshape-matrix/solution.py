import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    arr = np.array(a)
    rows, cols = new_shape
    
    # Ensure total elements match and dimensions are valid
    if rows <= 0 or cols <= 0 or arr.size != rows * cols:
        return []
    
    reshaped_matrix = arr.reshape(new_shape)
    return reshaped_matrix.tolist()