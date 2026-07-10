# 33. Evaluate a postfix expression using a Stack


def evaluate_postfix(expression):
    stack = []
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[token](a, b))
        else:
            raise ValueError(f"Unknown token: {token}")

    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")
    return stack[-1]


if __name__ == "__main__":
    expression = "7 8 + 3 2 + *"
    print("Result:", evaluate_postfix(expression))
