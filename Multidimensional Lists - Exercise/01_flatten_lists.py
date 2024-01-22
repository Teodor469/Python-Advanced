# matrix = [el.split() for el in input().split('|')]

# for cage in reversed(matrix):
#     if cage:
#         result = ' '.join(cage)
#         print(result, end=" ")

line = input().split("|")

sub_list = []

for sub_string in line[::-1]:
    sub_list.extend(sub_string.split())

print(*sub_list)