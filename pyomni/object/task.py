# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pyomni.config
import pyomni.util
import pyomni.object
from pyomni.object.base import OmniObjectBase


class OmniTask(OmniObjectBase):

    def __init__(self, name, added=None):
        super(OmniTask, self).__init__(name=name, added=added)
        return

    def get_xml(self):
        doc, root = pyomni.util.create_xml_base()

        task = doc.createElement("task")
        task.setAttribute("id", pyomni.util.generate_random_code())
        root.appendChild(task)

        added = doc.createElement("added")
        added_text = doc.createTextNode(self.get_formatted_added())
        added.appendChild(added_text)

        name = doc.createElement("name")
        name_text = doc.createTextNode(self.name)
        name.appendChild(name_text)

        task.appendChild(added)
        task.appendChild(name)

        doc.appendChild(root)
        return doc.toprettyxml(encoding="utf-8", indent="", newl="")
