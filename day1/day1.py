#!/usr/bin/env python3
import argparse
from math import prod


def part1(numbers):
    """ Finds 2 numbers in a list of numbers which added together equal 2020. """
    for a in numbers[:-1]:  # Skip last number, already checked
        b = 2020 - a
        if b in numbers:
            return a, b


def part2(numbers):
    """ Finds 3 numbers in a list of numbers which added together equal 2020. """
    for a in numbers:
        for b in numbers:
            c = 2020 - b - a
            if c in numbers:
                return a, b, c


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file containing a list of numbers")
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.filename) as f:
        numbers = [int(line) for line in f.read().splitlines()]

    # Part 1
    terms = part1(numbers)
    if terms is not None:
        print(prod(terms))

    # Part 2
    terms = part2(numbers)
    if terms is not None:
        print(prod(terms))


if __name__ == "__main__":
    main()
