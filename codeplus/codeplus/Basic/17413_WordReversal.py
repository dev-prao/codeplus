def print_stack(stack):
    while stack:
        print(stack.pop(), end='')


string = input()
tag = False
stack = []
for char in string:
    if char == '<':
        print_stack(stack)
        print(char, end='')
        tag = True

    elif char == '>':
        print(char, end='')
        tag = False

    elif tag:
        print(char, end='')

    else:
        if char == ' ' or char == '\n':
            print_stack(stack)
            print(char, end='')
        else:
            stack.append(char)

print_stack(stack)
print()
