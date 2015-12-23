# -*- coding: utf-8 -*-
from __future__ import absolute_import
import datetime
import xml.dom.minidom
import pyomni.config
import pyomni.util
from pyomni.object.base import OmniObjectBase


class OmniTask(OmniObjectBase):

    def __init__(self, name, added=None):
        super(OmniTask, self).__init__()
        self._name = name
        self._added = added if added is not None else datetime.datetime.utcnow()
        return

    def get_xml(self):
        doc = xml.dom.minidom.Document()
        el = doc.createElementNS(pyomni.config.NS, "omnifocus")
        el.setAttribute("app-id", pyomni.config.APP_ID)
        el.setAttribute("xmlns", pyomni.config.NS)

        task = doc.createElement("task")
        task.setAttribute("id", pyomni.util.get_random_code())
        el.appendChild(task)

        added = doc.createElement("added")
        added_text = doc.createTextNode(self.get_formatted_added())
        added.appendChild(added_text)

        name = doc.createElement("name")
        name_text = doc.createTextNode(self.name)
        name.appendChild(name_text)

        task.appendChild(added)
        task.appendChild(name)

        doc.appendChild(el)
        return doc.toprettyxml(encoding="utf-8", indent="", newl="")
