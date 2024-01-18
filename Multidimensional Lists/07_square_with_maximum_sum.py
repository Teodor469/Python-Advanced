rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(rows):
    row_values = [int(el) for el in input().split(', ')]
    matrix.append(row_values)

max_sum = float('-inf')
sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_under = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        total_sum = current_element + next_element + element_under + element_diagonal

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [[current_element, next_element], [element_under, element_diagonal]]

for row in sub_matrix:
    print(*row)

print(max_sum)
