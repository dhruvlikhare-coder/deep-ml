def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float] | int:
    # 1. Validate dimensions first (columns in each row must match length of b)
    if not a or any(len(row) != len(b) for row in a):
        return -1

    # 2. Compute dot product for each row
    result = []
    for row in a:
        row_dot = sum(x * y for x, y in zip(row, b))
        result.append(row_dot)

    return result