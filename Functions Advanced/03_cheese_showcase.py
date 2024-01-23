def sorting_cheeses(**kwargs):
    result = ""
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese_name, quantity in sorted_result:
        result += cheese_name + "\n"
        for q in sorted(quantity, reverse=True):
            result += quantity + "\n"