def call_once(func):
    """Run a function or method once."""
    have_result = False

    def call_once_wrapper(*args, **kwargs):
        nonlocal have_result

        if have_result:
            return None

        have_result = True

        return func(*args, **kwargs)

    return call_once_wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b
