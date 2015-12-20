# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys
import io
import zipfile
import logging
import datetime

from .util import get_random_code
from .webdav.WebdavClient import CollectionStorer
from .webdav.WebdavClient import ResourceStorer
from .webdav.WebdavClient import parseDigestAuthInfo
from .webdav.Connection import AuthorizationError

OMNI_SERVER_BASE_URL = "https://sync1.omnigroup.com/"
logging.disable(logging.INFO)


def digest(storer):
    def _digest(func):
        def __digest(*args, **kwargs):
            self = args[0]
            if len(args) > 1 and isinstance(args[1], (str, unicode)):
                if args[1][0] != "/":
                    url = self.base_url + "/" + args[1]
                else:
                    url = self.base_url + args[1]
            else:
                url = self.base_url

            conn = storer(url, validateResourceNames=False)
            try:
                conn.readAllProperties()
            except AuthorizationError as e:
                if e.authType == "Digest":
                    info = parseDigestAuthInfo(e.authInfo)
                    conn.connection.addDigestAuthorization(
                        self.username, self.password,
                        realm=info["realm"],
                        qop=info["qop"],
                        nonce=info["nonce"]
                    )
                else:
                    raise
            args = args + (conn, )
            result = func(*args, **kwargs)
            return result
        return __digest
    return _digest


class PyOmni(object):

    BASE_HOST = "https://sync1.omnigroup.com"
    BASE_URL = BASE_HOST + "/{}/OmniFocus.ofocus/"

    def __init__(self, username, password):
        """Create PyOmni instance
        :param str username:
        :param str password:
        :return:
        """
        self._username = username
        self._password = password
        self._base_url = PyOmni.BASE_URL.format(username)
        return

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def base_url(self):
        return self._base_url

    @staticmethod
    def create_zip_name(last_id):
        now = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        return "{}={}+{}.zip".format(
            now, last_id, get_random_code()
        )

    @staticmethod
    def create_zip_body(file_list, write=False):
        if write:
            fo = "sample.zip"
        else:
            fo = io.BytesIO()

        with zipfile.ZipFile(fo, "w") as fh:
            for fd in file_list:
                fh.writestr(fd[0], fd[1])

        if write:
            return
        return fo.getvalue()

    @staticmethod
    def unzip_body(buf):
        fo = io.BytesIO(buf)
        zf = zipfile.ZipFile(fo)
        file_list = []
        for zip_file in zf.infolist():
            with zf.open(zip_file.filename) as fh:
                file_info = [
                    zip_file.filename,
                    fh.read()
                ]
                file_list.append(file_info)
        return file_list

    @digest(CollectionStorer)
    def ls(self, conn):
        file_list = []
        for resource, properties in conn.getCollectionContents():
            file_list.append(resource.path.encode(sys.getfilesystemencoding()))
        return file_list

    @digest(CollectionStorer)
    def get_last_id(self, conn):
        """Return latest transaction id
        :param conn:
        :rtype: str | None
        """
        zip_file_list = []
        for resource, properties in conn.getCollectionContents():
            ext = resource.path.encode(sys.getfilesystemencoding()).split('.')[-1]
            if ext == "zip":
                zip_file_list.append(resource.path.encode(sys.getfilesystemencoding()))

        if len(zip_file_list) > 0:
            zip_file_list.sort()
            return zip_file_list[-1].split("+")[1].split(".")[0]
        return None

    @digest(ResourceStorer)
    def get_content(self, file_path, conn):
        buf = conn.downloadContent().read()

        if file_path.split('.')[-1] == "zip":
            fo = io.BytesIO(buf)
            zf = zipfile.ZipFile(fo)
            file_list = []
            for zip_file in zf.infolist():
                with zf.open(zip_file.filename) as fh:
                    file_info = [
                        zip_file.filename,
                        fh.read()
                    ]
                    file_list.append(file_info)
        else:
            file_list = [
                file_path.split('/')[-1],
                buf
            ]

        return file_list

    @digest(ResourceStorer)
    def upload_content(self, file_path, buf, conn):
        conn.uploadContent(buf)

    @digest(ResourceStorer)
    def delete_content(self, file_path, conn):
        conn.deleteContent()

    @digest(ResourceStorer)
    def rm(self, file_path, conn):
        conn.delete()

    def add_task(self, task):
        """Add task to Omnifocus sync server
        :param OmniTask task:
        :return:
        """
        last_id = self.get_last_id()
        zip_name = PyOmni.create_zip_name(last_id)
        zip_buf = PyOmni.create_zip_body([[
            "contents.xml",
            task.get_xml()
        ]])
        self.upload_content(zip_name, zip_buf)
        return
