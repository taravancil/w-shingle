#!/usr/bin/python
import argparse

def main(argv):
    # Define arguments
    parser = argparse.ArgumentParser(description="Transform a \
    string into tokens of length w.")
    parser.add_argument("string", type=str, help="the string to \
    tokenise")
    parser.add_argument("-w", type=int, default=3, help="the \
    number of words per shingle")

    args = parser.parse_args(argv[1:])

    try:
        print w_shingle(args.string, args.w)
    except Exception as err:
        print err
        parser.print_help()

def w_shingle(string, w):
    """Return the set of contiguous sequences (shingles) of `w` words
    in `string`."""
    words = string.split()
    tokens = []
    num_words = len(words)
    i = 0

    # Confirm that 0 < `w` <= `num_words`
    if w > num_words or w == 0:
        raise Exception('Invalid argument -w')

    # If w is equal to the number of words in the input string, the
    # only item in the set is `words`.
    if w == num_words:
        tokens.append(words)
        return tokens

    while i <= num_words - w:
        # Get a token of w words
        token = words[i:i+w]

        if token not in tokens:
            tokens.append(token)

        i += 1

    return tokens

if __name__ == "__main__":
    import sys
    main(sys.argv)
