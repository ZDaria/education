def binary_search(var_list: list, item: int):

    low = 0
    high = len(var_list) - 1
    while low <= high:
        mid = low + high
        guess = var_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid + 1
    return None
