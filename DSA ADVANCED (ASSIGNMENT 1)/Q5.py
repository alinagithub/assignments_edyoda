def find_duplicates(arr):
    """
    Find and return duplicates in an array.

    Args:
        arr (list): The input array.

    Returns:
        list: A list containing the duplicate elements found in the array.
    """
    duplicates = set()
    result = []

    for num in arr:
        if num in duplicates and num not in result:
            result.append(num)
        else:
            duplicates.add(num)

    return result


# Example usage:
arr = [1, 2, 3, 4, 2, 5, 6, 3, 7, 7, 8, 9, 9]
duplicates = find_duplicates(arr)
print("Duplicates in the array are:", duplicates)