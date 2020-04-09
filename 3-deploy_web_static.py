#!/usr/bin/python3

from fabric.api import *
from datetime import datetime
from os.path import getsize, isfile


env.hosts = [
    '104.196.117.221',
    '54.221.125.45',
]


@runs_once
def do_pack():
    """ generate a .tgz archive from the contents of the web_static folder """

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    folder = local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(now)
    files = local("tar -cvzf {} ./web_static".format(path))
    size_file = getsize(path)
    if folder.succeeded and files.succeeded:
        msg = "web_static packed: {} -> {}Bytes".format(path, size_file)
        print(msg)
        return path
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to your web servers """
    if isfile(archive_path):

        upload = put(archive_path, "/tmp/")

        name_file = archive_path.split('/')[-1].split('.')[0]
        path_to_unpack = "/data/web_static/releases/{}".format(name_file)
        unpack_command = "tar -xzf /tmp/{}.tgz -C {}"
        mv_command = "mv {0}/web_static/* {0}/"
        mkdir_command = "mkdir -p /data/web_static/releases/{}/"

        mkdir = sudo(mkdir_command.format(name_file))

        unpackt_file = sudo(unpack_command.format(name_file, path_to_unpack))

        rm_file = sudo("rm /tmp/{}.tgz".format(name_file))

        move_files = sudo(mv_command.format(path_to_unpack))

        # delete old webstatic

        # delete symbolink link
        delete_symb = sudo("rm -rf /data/web_static/current")

        make_symb = sudo(
            "ln -sf {} /data/web_static/current".format(path_to_unpack)
        )

        operations = [
            upload,
            mkdir,
            unpackt_file,
            rm_file,
            move_files,
            delete_symb,
            make_symb,
        ]

        print("New version deployed!")
        return all([operation.succeeded for operation in operations])

    else:
        return False


def deploy():
    """ creates and distributes an archive to your web servers """

    archive_path = do_pack()

    if archive_path:
        return do_deploy(archive_path)
    else:
        return False
