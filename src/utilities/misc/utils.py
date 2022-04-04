

def decompose_to_lists(list_of_tuples):
    """Converts the list of (key, value) tuples into two lists - one with keys and second with values."""

    keys = []
    values = []

    # iterating over the tuples lists
    for (key, value) in list_of_tuples:
        keys.append(key)
        values.append(value)

    return keys, values
