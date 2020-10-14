import string

def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    # The subset on which we are operating.
    subset = alpha[:size]
    inverse_subset = reversed(subset)
    base = "-".join(inverse_subset)  # "e-d-c-b-a"
    rows = []
    # top-left square:
    for i in range(size):
        # Generate each row by removing trailing chars from the base string.
        row = base[:len(base) - i * 2]
        # Pad that row to match length of the base string
        row = ("-" * (len(base) - len(row))) + row
        rows.insert(0, row)
    # Now that upper left corner is generated, mirror it downwards like this,
    # without adding again the base string:
    rows.extend(reversed(rows[:-1]))
    # right square:
    for i in range(len(rows)):
        row = rows[i]
        # Reverse the row
        rev_row = row[::-1]
        # append the reversed row without the initial character
        rows[i] = row + rev_row[1:]
    print(*rows, sep="\n")


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)