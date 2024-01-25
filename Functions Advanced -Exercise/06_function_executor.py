def func_executor(*funcs_data):
    result = []

    for func, args in funcs_data:
        result.append(f"{func.__name__} - {func(*args)}")

    return "\n".join(result)