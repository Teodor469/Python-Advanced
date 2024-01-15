# n, m = [int(x) for x in input().split()]

# first_set = {input() for _ in  range(n)}
# second_set = {input() for _ in range(m)}

# print(*first_set.intersection(second_set), sep="\n")


#second solution
n, m = map(int, input().split())
first_set = set()
second_set = set()

for i in range(n+m):
    number = int(input())
    if i < n:
        first_set.add(number)
    else:
        second_set.add(number)

third_set = first_set & second_set
print(*third_set, sep="\n")


# & and, intersection
# | or, union
# - subtract, difference
# ^ symmetric, difference