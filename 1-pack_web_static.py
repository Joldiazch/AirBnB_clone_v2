#!/usr/bin/python3

from fabric.api import local
from datetime import datetime
from os.path import getsize

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
		return msg
	print(None)
	return None
