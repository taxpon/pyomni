# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime


class OmniObjectBase(object):

    def __init__(self, task_id=None, added=None,
                 modified=None, name=None, rank=None,
                 order="parallel", completed_by_children=False):
        """Create OmniObjectBase instance
        :param str task_id:
        :param datetime.datetime added:
        :param datetime.datetime modified:
        :param str name:
        :param int rank:
        :param string order:
        :param bool complete_by_children:
        :return:
        """
        self._task_id = task_id
        self._added = added if added is not None else datetime.datetime.utcnow()
        self._modified = modified
        self._name = name
        self._rank = rank
        self._order = order
        self._completed_by_children = completed_by_children

    @property
    def task_id(self):
        return self._task_id

    @property
    def added(self):
        return self._added

    @property
    def modified(self):
        return self._modified

    @property
    def name(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def rank(self):
        return self._rank

    @property
    def order(self):
        return self._order

    @property
    def completed_by_children(self):
        return self._completed_by_children

    def get_formatted_added(self):
        return self.added.isoformat()[:-3] + "Z"
