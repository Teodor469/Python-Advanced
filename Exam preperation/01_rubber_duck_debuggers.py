from collections import deque

def calculate_ducky(time_for_completion, number_of_tasks):
    ducky_counts = {
        "Darth Vader Ducky": 0,
        "Thor Ducky": 0,
        "Big Blue Rubber Ducky": 0,
        "Small Yellow Rubber Ducky": 0
    }

    while time_for_completion and number_of_tasks:
        sequence_calc = time_for_completion[0] * number_of_tasks[-1]
        ducky_type = ""

        if sequence_calc <= 60:
            ducky_type = "Darth Vader Ducky"
        elif sequence_calc <= 120:
            ducky_type = "Thor Ducky"
        elif sequence_calc <= 180:
            ducky_type = "Big Blue Rubber Ducky"
        elif sequence_calc <= 240:
            ducky_type = "Small Yellow Rubber Ducky"
        else:
            # If the calculated time goes above the highest range
            number_of_tasks[-1] -= 2  # decrease the number of the tasks' value by 2
            time_for_completion.append(time_for_completion.popleft())  # move the programmer time's value to the end of its sequence
            continue

        ducky_counts[ducky_type] += 1
        # Remove the used values
        time_for_completion.popleft()
        number_of_tasks.pop()

    # Output the type and number of ducks given
    for ducky, count in ducky_counts.items():
        print(f"{ducky}: {count}")

    return ducky_counts

# Test the function
time_for_completion = deque([int(el) for el in input().split()])
number_of_tasks = [int(el) for el in input().split()]
print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
calculate_ducky(time_for_completion, number_of_tasks)
