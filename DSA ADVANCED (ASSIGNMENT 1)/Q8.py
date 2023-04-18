#Reverse a string using a stack data structure
def reverse_string_using_stack(s):
    """
    Reverse a string using a stack data structure.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """
    stack = []
    for char in s:
        stack.append(char)  # Push each character onto the stack

    reversed_string = ''
    while len(stack) > 0:
        reversed_string += stack.pop()  # Pop each character from the stack and append to the reversed string

    return reversed_string


# Example usage:
input_string = "Hello, World!"
reversed_string = reverse_string_using_stack(input_string)
print("Original string:", input_string)
print("Reversed string:", reversed_string)