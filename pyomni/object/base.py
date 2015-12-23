# -*- coding: utf-8 -*-
from __future__ import absolute_import


class OmniObjectBase(object):
    
    def __init__(self):
        self._id = None
        self._added = None
        self._modified = None
        self._name = None
        self._rank = None
        self._order = None
        self._completed_by_children = None
    
    @property
    def id(self):
        return self._id

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
        return self.date.isoformat()[:-3] + "Z"
