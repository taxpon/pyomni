# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
import nose
from nose.tools import ok_, eq_

from pyomni.util import generate_random_code
from pyomni.util import create_xml_base
from pyomni.util import Validator


class TestUtil(object):

    def test_generate_random_code(self):
        code = generate_random_code()
        ok_(Validator.is_str(code))
        eq_(len(code), 11)

        code = generate_random_code(10)
        ok_(Validator.is_str(code))
        eq_(len(code), 10)

        code = generate_random_code(-1)
        eq_(code, None)

        code = generate_random_code("11")
        eq_(code, None)
        return

    def test_create_xml_base(self):
        doc, root = create_xml_base()
        doc.appendChild(root)
        xml = doc.toprettyxml(encoding="utf-8", indent="", newl="")
        correct_xml = '<?xml version="1.0" encoding="utf-8"?>' \
                      '<omnifocus app-id="com.omnigroup.OmniFocus2.MacAppStore"' \
                      ' xmlns="http://www.omnigroup.com/namespace/OmniFocus/v1"/>'
        eq_(xml, correct_xml)
        return


class TestValidator(object):

    def test_is_int(self):
        value = 1
        ok_(Validator.is_int(value))

        value = "1"
        ok_(not Validator.is_int(value))
        return

    def test_is_str(self):
        value = "str"
        ok_(Validator.is_str(value))

        value = 1
        ok_(not Validator.is_str(value))
        return

if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
