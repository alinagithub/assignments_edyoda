def count_pairs_with_sum(arr, target_sum):
    """
    Count the number of pairs in an array that sum up to a given target sum.

    Args:
        arr (list): The input array.
        target_sum (int): The target sum to be checked.

    Returns:
        int: The count of pairs that sum up to the target sum.
    """
    # Create a dictionary to store the frequency of array elements
    freq_map = {}
    count = 0  # Initialize the count of pairs to 0

    # Iterate through the array
    for num in arr:
        # Calculate the complement of the current element with respect to the target sum
        complement = target_sum - num

        # If the complement is present in the dictionary, increment the count of pairs
        if complement in freq_map:
            count += freq_map[complement]

        # Increment the frequency of the current element in the dictionary
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    return count


# Example usage:
arr = [1, 5, 3, 7, 9, 2, 8, 4]
target_sum = 10
result = count_pairs_with_sum(arr, target_sum)
print("Number of pairs with sum", target_sum, "is:", result)