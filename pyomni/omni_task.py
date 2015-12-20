# -*- coding: utf-8 -*-
import datetime
import xml.dom.minidom
import util

NS = 'http://www.omnigroup.com/namespace/OmniFocus/v1'
APP_ID = 'com.omnigroup.OmniFocus2.MacAppStore'


class OmniTask(object):

    def __init__(self, name, date=None, project=None, context=None):
        self._name = name

        if date is None:
            self._date = datetime.datetime.utcnow()
        else:
            self._date = date

        self._project = project
        self._context = context

    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def project(self):
        return self._project

    @property
    def context(self):
        return self._context

    def get_formatted_date(self):
        return self.date.isoformat()[:-3] + "Z"

    def get_xml(self):
        """Return XML formatted task information
        :rtype: str
        """
        doc = xml.dom.minidom.Document()
        el = doc.createElementNS(NS, "omnifocus")
        el.setAttribute("app-id", APP_ID)
        el.setAttribute("xmlns", NS)

        task = doc.createElement("task")
        task.setAttribute("id", util.get_random_code())
        el.appendChild(task)

        added = doc.createElement("added")
        added_text = doc.createTextNode(self.get_formatted_date())
        added.appendChild(added_text)

        name = doc.createElement("name")
        name_text = doc.createTextNode(self.name)
        name.appendChild(name_text)

        task.appendChild(added)
        task.appendChild(name)

        doc.appendChild(el)
        return doc.toprettyxml(encoding="utf-8", indent="", newl="")

if __name__ == "__main__":
    ot = OmniTask("hogehoge")
    print ot.get_xml()
