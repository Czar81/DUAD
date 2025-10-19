
def filter_locals(locals_dict: dict, exclude: tuple = ("self",)):
    return {k: v for k, v in locals_dict.items() if k not in exclude}
