# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            # Check for empty or invalid
            if len(opening_brackets_stack) == 0 or not (are_matching(opening_brackets_stack[-1].char, next)):
                print(i + 1)
                exit()
            else:
                opening_brackets_stack.pop()
    return opening_brackets_stack


def main():
    text = input()
    if "F" in text:
        file = open("./test/5", "r")
        text = file.read()
    elif "I" in text:
        text = input()

    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if len(mismatch) == 0:
        print("Success")
    else:
        print(mismatch[-1].position)


if __name__ == "__main__":
    main()
