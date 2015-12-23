# -*- coding: utf-8 -*-
import datetime
import nose
from nose.tools import assert_equal

from pyomni.object.task import OmniTask


class TestOmniTask(object):

    def test_get_formatted_date(self):
        dt = datetime.datetime(year=2015, month=1, day=23, hour=4, minute=5, second=6, microsecond=123456)
        ot = OmniTask("test", added=dt)
        assert_equal(ot.get_formatted_added(), "2015-01-23T04:05:06.123Z")
        return

if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
