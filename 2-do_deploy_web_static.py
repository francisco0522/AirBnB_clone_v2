#!/usr/bin/python3
"generates a .tgz archive from the contents of the web_static"
from fabric.api import local, put, run, env
from os import path
from datetime import datetime
from shlex import split

env.user = 'ubuntu'
env.hosts = ["35.243.229.224", "34.229.175.198"]


def do_deploy(archive_path):
    "distributes an archive to your web servers"
    if not path.exists(archive_path) or (
                                         path.exists(archive_path) and
                                         path.isdir(archive_path)):
        return False
    try:
        put(archive_path, '/tmp/')
        name = archive_path.split("/")[1]
        fil = name.split(".")[0]
        create = "mkdir -p /data/web_static/releases/{}/".format(fil)
        run(create)
        uncompress = "tar -xzf /tmp/{} -C ".format(name)
        uncompress += "/data/web_static/releases/{}/".format(fil)
        run(uncompress)
        delete = "rm /tmp/{}".format(name)
        run(delete)
        move = "mv /data/web_static/releases/{}".format(fil)
        move += "/web_static/* "
        move += "/data/web_static/releases/{}/".format(fil)
        run(move)
        deleteFolder = "rm -rf /data/web_static/releases/{}".format(fil)
        deleteFolder += "/web_static"
        run(deleteFolder)
        deleteLink = "rm -rf /data/web_static/current"
        run(deleteLink)
        createLink = "ln -s /data/web_static/releases/{}/ ".format(name)
        createLink += "/data/web_static/current"
        run(createLink)
        return True
    except Exception:
        return False
