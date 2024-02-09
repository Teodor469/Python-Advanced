def gather_credits(number_of_credits_needed, *args):
    enrolled_courses = set()
    total_credits = 0

    for course_name, credits in args:
        if course_name not in enrolled_courses:
            enrolled_courses.add(course_name)
            total_credits += credits

        if total_credits >= number_of_credits_needed:
            sorted_courses = sorted(enrolled_courses)
            return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted_courses)}"

    credits_shortage = number_of_credits_needed - total_credits
    return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."