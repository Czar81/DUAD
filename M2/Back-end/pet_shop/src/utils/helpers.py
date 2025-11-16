def filter_values(locals_dict: dict, exclude: tuple = ("self",)):
    return {k: v for k, v in locals_dict.items() if k not in exclude and v is not None}

def generate_cache_based_filters(key_prefix:str, filter_dict:dict):
    value_filters=filter_values(locals_dict)
    if value_filters:
        cache_suffix = ":".join(f"{k}={v}" for k, v in sorted(value_filters.items()))
        return f"{key_prefix}:{cache_suffix}"
    else:
        return f"{key_prefix}:all"

def generate_cache_key(key_prefix, id_product):
    return f"{key_prefix}:{id_product}"