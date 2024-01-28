# def  softuni_students(*args, **kwargs):
#     course_id, username = args[0]

#     for key, value in kwargs.items():
#         if course_id == key:
#             pass

def softuni_students(*args, **kwargs):
    students = {}
    courses = kwargs
    invalid_students = []

    for arg in args:
        course_id, username = arg
        if course_id in courses:
            if course_id not in students:
                students[course_id] = []
            students[course_id].append(username)
        else:
            invalid_students.append(username)

    result = ""
    for course_id, usernames in sorted(students.items(), key=lambda item: sorted(item[1])):
        for username in usernames:
            result += f"*** A student with the username {username} has successfully finished the course {courses[course_id]}!\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result.strip()


student_data = [
    ('id_4', 'John'),
    ('id_4', 'Alice'),
    ('id_4', 'Bob'),
    ('id_4', 'Eve'),
]
course_data = {
    'id_4': 'Course 1',
}

result = softuni_students(*student_data, **course_data)
print(result)
