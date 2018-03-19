import re


def validate_pin(pin):
    is_valid4 = re.search(r'^[0-9]{4}$', pin)
    is_valid6 = re.search(r'^[0-9]{6}$', pin)
    if is_valid4 or is_valid6:
        return True
    else:
        return False


# int(pin).isnumeric() and isinstance(pin, int) and

print(validate_pin("11023"))

