# -*- coding: utf-8 -*-
import datetime
import nose
from nose.tools import eq_
from pyomni.object.base import OmniObjectBase


class TestOmniObjectBase(object):

    def test_init(self):
        task_id, added, modified, name, rank, order, complete_by_children = ("1", "2", "3", "4", "5", "6", "7")
        oob = OmniObjectBase(task_id, added, modified, name,
                             rank, order, complete_by_children)

        eq_(oob.task_id, "1")
        eq_(oob.added, "2")
        eq_(oob.modified, "3")
        eq_(oob.name, "4")
        eq_(oob.rank, "5")
        eq_(oob.order, "6")
        eq_(oob.completed_by_children, "7")
        return

    def test_get_formatted_added(self):
        dt = datetime.datetime(
            year=2015, month=1, day=23,
            hour=4, minute=5, second=6, microsecond=123456
        )
        ot = OmniObjectBase("test", added=dt)
        eq_(ot.get_formatted_added(), "2015-01-23T04:05:06.123Z")
        return

if __name__ == '__main__':
    nose.main(argv=['nosetests', '-s', '-v'], defaultTest=__file__)
