#!/usr/bin/env python3
import argparse


def parse_password_line(line):
    """ Separates out the password from the password policy. """
    policy, password = line.split(":")
    return policy.strip(), password.strip()


def parse_password_policy(password_policy):
    """ Determines from the policy the number of times a letter may be repeated """
    allowed_range, letter = password_policy.split(" ")
    min_count, max_count = allowed_range.split("-")
    return int(min_count), int(max_count), letter


def part1(password_lines):
    """ Determines the number of valid passwords given min and max letter counts """
    valid_passwords = 0
    for line in password_lines:
        policy, password = parse_password_line(line)
        min_count, max_count, letter = parse_password_policy(policy)

        if password.count(letter) >= min_count and password.count(letter) <= max_count:
            valid_passwords = valid_passwords + 1
    return valid_passwords


def part2(password_lines):
    """
    Determines the number of valid passwords given two positions in the password.
    The letter must occur in either position but not both.
    """
    valid_passwords = 0
    for line in password_lines:
        policy, password = parse_password_line(line)
        pos_a, pos_b, letter = parse_password_policy(policy)

        chr_a = password[pos_a - 1]
        chr_b = password[pos_b - 1]

        if letter in (chr_a, chr_b) and chr_a != chr_b:
            valid_passwords = valid_passwords + 1
    return valid_passwords


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="password file")
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.filename) as f:
        password_lines = [line.strip() for line in f.read().splitlines()]

    # Part 1
    valid_passwords_1 = part1(password_lines)
    print(valid_passwords_1)

    # Part2
    valid_passwords_2 = part2(password_lines)
    print(valid_passwords_2)


if __name__ == "__main__":
    main()
