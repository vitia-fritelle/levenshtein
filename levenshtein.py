
def fill_first_row(matrix: list, index: int = 0, edits: int = 0) -> list:
    row: list = matrix[0]
    if index < len(row):
        matrix[0][index] = edits
        return fill_first_row(matrix, index+1, edits+1)
    else:
        return matrix

def fill_first_column(matrix: list, index: int = 0, edits: int = 0) -> list:
    if index < len(matrix):
        matrix[index][0] = edits
        return fill_first_column(matrix, index+1, edits+1)
    else:
        return matrix

def edit_distance(input: str, target: str):
    N_input = len(input)+1
    N_target = len(target)+1
    cache = [[float("inf")]*N_input for _ in range(N_target)]
    fill_first_row(cache)
    fill_first_column(cache)
    edit_distance_iteration(input, target, cache)
    return cache[N_target-1][N_input-1]

def edit_distance_iteration(input: str, target: str, cache: list,
    input_index: int = 1, target_index: int = 1):
    N_input = len(input)+1
    N_target = len(target)+1
    if input_index < N_input and target_index < N_target:
        base = min((
            cache[target_index-1][input_index-1],
            cache[target_index-1][input_index],
            cache[target_index][input_index-1],
        ))
        if input[input_index-1] == target[target_index-1]:
            cache[target_index][input_index] = base
        else:
            cache[target_index][input_index] = base+1
        edit_distance_iteration(input, target, cache, input_index, target_index+1)
        edit_distance_iteration(input, target, cache, input_index+1, target_index)
        edit_distance_iteration(input, target, cache, input_index+1, target_index+1)


if __name__ == "__main__":
    print(f"The least number of edits is {edit_distance('abacaxi', 'banana')}")