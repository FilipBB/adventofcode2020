#!/usr/bin/env python3
import argparse
import re


req_field_patterns = {
    "byr": r"\d{4}$",
    "iyr": r"\d{4}$",
    "eyr": r"\d{4}$",
    "hgt": r"\d+cm|\d+in$",
    "hcl": r"#[0-9a-f]{6}$",
    "ecl": r"amb|blu|brn|gry|grn|hzl|oth$",
    "pid": r"\d{9}$",
    # "cid": "Country ID" is optional
}


def valid_passport_field(k, v):
    """ Validate passport field by regex match and integer value """
    if k == "byr":
        if not (int(v) >= 1920 and int(v) <= 2002):
            return False
    elif k == "iyr":
        if not (int(v) >= 2010 and int(v) <= 2020):
            return False
    elif k == "eyr":
        if not (int(v) >= 2020 and int(v) <= 2030):
            return False
    elif k == "hgt":
        if "cm" in v:
            height_cm = v.replace("cm", "")
            if not (int(height_cm) >= 150 and int(height_cm) <= 193):
                return False
        elif "in" in v:
            height_in = v.replace("in", "")
            if not (int(height_in) >= 59 and int(height_in) <= 76):
                return False

    try:
        pattern = re.compile(req_field_patterns[k])
        if not pattern.match(v):
            return False
    except KeyError:  # Ignore keys we don't know about
        pass

    return True


def parse_passport(raw_passport):
    """ Parse raw passport data into a dict """
    passport_data = raw_passport.split(" ")
    passport = {}
    for data in passport_data:
        k, v = data.split(":")
        passport.update({k: v})
    return passport


def parse_passport_file(filename):
    """ Parse a passport text file into a list of passports """
    with open(filename) as f:
        passports = []
        passport_lines = []

        for line in f.read().splitlines():
            if not line:
                # blank lines separate passports, add the current
                # passport and continue to the next one
                if passport_lines:
                    raw_passport = " ".join(passport_lines)
                    passport = parse_passport(raw_passport)
                    passports.append(passport)
                passport_lines = []
                continue
            passport_lines.append(line)

        # if the last line is not empty don't forget to append the last passport
        if passport_lines:
            raw_passport = " ".join(passport_lines)
            passport = parse_passport(raw_passport)
            passports.append(passport)
    return passports


def complete_passport(passport):
    """ Ensure passport contains all required data. """
    for field in req_field_patterns:
        if field not in passport:
            return False
    return True


def get_args():
    parser = argparse.ArgumentParser(description="print the number of valid passports")
    parser.add_argument("filename", help="file containing passports")
    return parser.parse_args()


def main():
    args = get_args()
    passports = parse_passport_file(args.filename)

    # Part 1
    complete_passports = [p for p in passports if complete_passport(p)]
    print(len(complete_passports))

    # Part 2
    valid_passports = 0
    for passport in complete_passports:
        for k, v in passport.items():
            if not valid_passport_field(k, v):
                break
        else:
            valid_passports = valid_passports + 1
    print(valid_passports)


if __name__ == "__main__":
    main()
