from random import randint


def generate_validation_code():
    return "{:04d}".format(randint(0, 99999))


def validate_validation_code(validation_code: int):
    return validation_code




