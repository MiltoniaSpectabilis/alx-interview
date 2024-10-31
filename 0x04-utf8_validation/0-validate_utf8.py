#!/usr/bin/python3

""" a UTF-8 Validation function """


def validUTF8(data):
    """ Validate UTF-8 """
    def get_byte_count(byte):
        if byte >> 7 == 0:
            return 1
        elif byte >> 5 == 0b110:
            return 2
        elif byte >> 4 == 0b1110:
            return 3
        elif byte >> 3 == 0b11110:
            return 4
        return -1

    def is_valid_following_byte(byte):
        """ Check if a byte is a valid UTF-8 following byte """
        return byte >> 6 == 0b10

    i = 0
    while i < len(data):
        byte_count = get_byte_count(data[i])
        if byte_count == -1:
            return False
        for j in range(1, byte_count):
            if i + j >= len(data) or not is_valid_following_byte(data[i + j]):
                return False
        i += byte_count
    return True
