#Evaluate a postfix expression using stack?
def evaluate_postfix_expression(expression):
    """
    Evaluate a postfix expression using a stack data structure.

    Args:
        expression (str): The postfix expression to be evaluated.

    Returns:
        int/float: The result of the evaluated postfix expression.
    """
    stack = []
    operators = ['+', '-', '*', '/']

    for char in expression:
        if char not in operators:
            # If the character is a digit, push it onto the stack
            stack.append(float(char))
        else:
            # If the character is an operator, pop the top two elements from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Evaluate the expression based on the operator
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)

    # The final result of the postfix expression will be left on the stack
    return stack[0]


# Example usage:
postfix_expr = "53+62/*35*+"
result = evaluate_postfix_expression(postfix_expr)
print("Postfix Expression:", postfix_expr)
print("Result:", result)