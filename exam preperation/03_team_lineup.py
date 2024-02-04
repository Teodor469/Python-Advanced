def team_lineup(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))