def remember_result(func):
    """Remembers last result of function it decorates and prints it before next call."""
    last_result = None

    def print_last_result(*args, **kwargs):
        nonlocal last_result

        print(f"Last result = '{last_result}'")
        last_result = func(*args, **kwargs)

        return last_result

    return print_last_result


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += item
        print(f"Current result = '{result}'")
    return result
