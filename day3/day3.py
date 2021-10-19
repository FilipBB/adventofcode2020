#!/usr/bin/env python3
import argparse
from math import prod


def extend_pattern(pattern):
    """ Extends the given pattern by making one copy to the right """
    extended_pattern = []
    for line in pattern:
        new_line = line + line
        extended_pattern.append(new_line)
    return extended_pattern


def count_trees(x_travel, y_travel, pattern):
    x = 0
    y = 0
    tree = "#"
    num_trees = 0

    while y < len(pattern):
        # if we're out of range width-wise, extend the pattern
        while x >= len(pattern[y]):
            pattern = extend_pattern(pattern)

        # check for a tree at the current coordinates
        if pattern[y][x] == tree:
            num_trees = num_trees + 1

        x = x + x_travel
        y = y + y_travel

    return num_trees


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file containing pattern")
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.filename) as f:
        pattern = [line for line in f.read().splitlines()]

    # Part 1
    num_trees = count_trees(3, 1, pattern)
    print(num_trees)

    # Part 2
    trees_in_paths = []
    for x_travel, y_travel in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        num_trees = count_trees(x_travel, y_travel, pattern)
        trees_in_paths.append(num_trees)
    print(prod(trees_in_paths))


if __name__ == "__main__":
    main()
