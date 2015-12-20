from __future__ import absolute_import
import logging
import random
import string


def get_random_code(length=11):

    if length is None:
        Error.invalid_type(Error.INT, "length")
        return None

    if length <= 0:
        return None

    char_list = string.digits + string.letters + "_-"
    return ''.join(random.choice(char_list) for i in xrange(length))


class Error(object):

    INT = "int"
    STR = "str"

    @staticmethod
    def log(msg):
        logging.error(msg)

    @staticmethod
    def invalid_type(type, variable_name="value"):
        Error.log("{} must be a {}.".format(variable_name, type))
        return
