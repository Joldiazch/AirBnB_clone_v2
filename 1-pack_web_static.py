#!/usr/bin/python3

from fabric.api import *
from fabric.decorators import runs_once
from datetime import datetime
from os.path import getsize

@runs_once
def do_pack():
    """ generate a .tgz archive from the contents of the web_static folder """

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    folder = local("mkdir versions")
    path = "versions/web_static_{}.tgz".format(now)
    files = local("tar -cvzf {} ./web_static".format(path))
    size_file = getsize(path)
    if folder.succeeded and files.succeeded:
        msg = "web_static packed: {} -> {}Bytes".format(path, size_file)
        print(msg)
        return path
    print(None)
    return None
