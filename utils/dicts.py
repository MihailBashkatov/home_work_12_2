def get_val(collection: dict, key, default='git'):
    if collection.get(key):
        return collection[key]
    return default
