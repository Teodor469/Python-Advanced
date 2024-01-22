matrix = [el.split() for el in input().split('|')]

for cage in reversed(matrix):
    if cage:
        result = ' '.join(cage)
        print(result, end=" ")
