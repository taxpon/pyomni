# -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
import random
import string
import xml.dom.minidom
import pyomni.config


def generate_random_code(length=11):
    """Generate random code. Main purpose of this function is to generate task id
    :param int length:
    :return: generated random code
    :rtype: str | None
    """

    if not Validator.is_int(length):
        Error.invalid_type(Error.INT, "length")
        return None

    if length <= 0:
        Error.log("Length must be a positive number.")
        return None

    char_list = string.digits + string.letters + "_-"
    return ''.join(random.choice(char_list) for i in xrange(length))


def create_xml_base():
    """Create base xml to control Omnifocus data
    :rtype: list of (xml.dom.minidom.Document, xml.dom.minidom.Element)
    """
    doc = xml.dom.minidom.Document()
    root = doc.createElementNS(pyomni.config.NS, "omnifocus")
    root.setAttribute("app-id", pyomni.config.APP_ID)
    root.setAttribute("xmlns", pyomni.config.NS)
    return doc, root


class Error(object):

    INT = "int"
    STR = "str"

    @staticmethod
    def log(msg):
        logging.error(msg)

    @staticmethod
    def invalid_type(type_name, variable_name="value"):
        Error.log("{} must be a {}.".format(variable_name, type_name))
        return


class Validator(object):

    @staticmethod
    def is_int(value):
        return isinstance(value, (int, long))

    @staticmethod
    def is_str(value):
        return isinstance(value, (str, unicode))
