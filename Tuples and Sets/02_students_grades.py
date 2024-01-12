n = int(input())

student_grades = {}

for _ in range(n):
    name, grade = input().split()
    grade_float = float(grade)

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade_float)

for name, grades in student_grades.items():
    avg_grade = sum(grades) / len(grades)
    formatted = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{name} -> {formatted} (avg: {avg_grade:.2f})")
