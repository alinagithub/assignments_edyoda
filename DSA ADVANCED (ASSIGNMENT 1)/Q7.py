#Move all the negative elements to one side of the array
def move_negative_to_one_side(arr):
    """
    Move all the negative elements to one side of the array.

    Args:
        arr (list): The input array.

    Returns:
        list: The updated array with all negative elements moved to one side.
    """
    # Initialize pointers for left and right ends of the array
    left = 0
    right = len(arr) - 1

    # Loop through the array until left and right pointers meet
    while left <= right:
        # If the element at left pointer is negative, move to the next element
        if arr[left] < 0:
            left += 1
        # If the element at right pointer is positive, move to the previous element
        elif arr[right] >= 0:
            right -= 1
        # If the element at left pointer is positive and the element at right pointer is negative,
        # swap them and move the pointers towards each other
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


# Example usage:
arr = [-3, 2, 1, -5, 6, -8, 9, -4, 7]
updated_arr = move_negative_to_one_side(arr)
print("Array with negative elements moved to one side:", updated_arr)