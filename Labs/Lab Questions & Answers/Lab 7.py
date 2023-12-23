import re

#part 1

def validate_variable(value):
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

    match = pattern.match(value)

    return bool(match)

#part 2

def validate_domain(value):
    pattern = re.compile(r'^[a-z][a-z0-9_]*(\.[a-z0-9_]+)*\.(com|ca|org)$', re.IGNORECASE)

    match = pattern.fullmatch(value)

    return bool(match)


def validate_phone(value):
    pattern = re.compile(r'^(\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\d{3}-\d{4})$')

    match = pattern.fullmatch(value)

    return bool(match)
