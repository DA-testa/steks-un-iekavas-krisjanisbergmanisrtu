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
            if not (len(opening_brackets_stack)):
                print("len = 0")

            if not (are_matching(opening_brackets_stack[-1].char, next)):
                print(opening_brackets_stack[-1].char + " is not " + next)

            if not (len(opening_brackets_stack)) or not (are_matching(opening_brackets_stack[-1].char, next)):
                print(i + 1)
            exit()
            else:
            opening_brackets_stack.pop()
    return opening_brackets_stack


def main():
    text = input()
    if text == "F":
        file = open("./test/0", "r")
        text = file.read()
    elif text == "I":
        text = input()

    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if len(mismatch) == 0:
        print("Success")
    else:
        print(mismatch[-1].position)


if __name__ == "__main__":
    main()
