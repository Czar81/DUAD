def _filter_locals(table, locals_dict: dict, exclude: tuple = ("self",)):
    filtered = {
        k: v for k, v in locals_dict.items() if k not in exclude and v is not None
    }
    return [getattr(table.c, k) == v for k, v in filtered.items()]
