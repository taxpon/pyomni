# -*- coding: utf-8 -*-
from __future__ import absolute_import
from pyomni.object.base import OmniObjectBase


class ProjectInfo(object):

    def __init__(self):
        self._folder_idref = None
        self._last_review = None
        self._review_interval = None

    @property
    def folder_idref(self):
        return self._folder_idref

    @property
    def last_review(self):
        return self._last_review

    @property
    def review_interval(self):
        return self._review_interval


class OmniProject(OmniObjectBase):

    def __init__(self):
        super(OmniProject, self).__init__()
        self._project_info = ProjectInfo()

    @property
    def project_info(self):
        return self._project_info
