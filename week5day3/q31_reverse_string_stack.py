# 31. Reverse a string using a Stack


def reverse_string(text):
    stack = []
    for char in text:
        stack.append(char)

    reversed_text = []
    while stack:
        reversed_text.append(stack.pop())

    return "".join(reversed_text)


if __name__ == "__main__":
    sample = "python"
    print("Reversed string:", reverse_string(sample))
