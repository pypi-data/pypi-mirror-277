def get_prefix(func, decorator_name):
    return f"{decorator_name.ljust(8)} | {func.__name__.ljust(16)}"
