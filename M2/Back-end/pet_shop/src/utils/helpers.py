
def filter_values(locals_dict: dict, exclude: tuple = ("self",)):
    return {k: v for k, v in locals_dict.items() if k not in exclude and v is not None}


def generate_cache_based_filters(key_prefix: str, filters_dict: dict):
    value_filters = filter_values(filters_dict)
    if value_filters:
        cache_suffix = ":".join(f"{k}={v}" for k, v in sorted(value_filters.items()))
        return f"{key_prefix}:{cache_suffix}"
    else:
        return f"{key_prefix}:all"


def generate_cache_key(key_prefix, id):
    return f"{key_prefix}:{id}"


def get_cache_if_exist(key, cache_manager, db_manager, **search_params):
    result = cache_manager.get_data(key)
    if result is None:
        result = db_manager.get_data(**search_params)
        if result == "Not found":
            return "Could not find any item", 404
        cache_manager.store_data(key, result)
    return result, 200
