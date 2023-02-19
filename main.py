# python3
def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        if next in ")]}":
            if((len(opening_brackets_stack) == 0) or not (are_matching(opening_brackets_stack[-1], next))):
                return i+1
            opening_brackets_stack.pop()
    return 0
    


def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch == 0):
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
