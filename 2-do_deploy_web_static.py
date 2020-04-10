#!/usr/bin/python3
"generates a .tgz archive from the contents of the web_static"
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import isfile

env.hosts = ["35.243.229.224", "34.229.175.198"]

def do_pack():
    "generates a .tgz archive"
    local("mkdir -p versions")
    timeNow = datetime.now()
    tgz = "versions/web_static_"
    tgz += "{}{}{}".format(timeNow.year, timeNow.month, timeNow.day)
    tgz += "{}{}{}".format(timeNow.hour, timeNow.minute, timeNow.second)
    tgz += ".tgz"
    result = "tar -cvzf "
    result += tgz
    result += " web_static"
    if local(result) == 1:
        return None
    return tgz

def do_deploy(archive_path):
    "distributes an archive to your web servers"
    if isfile(archive_path) is False:
        return False
    try:
        name = archive_path.split("/")[1]
        fil = archive_path.split("/")[1].split(".")[0]
        put(archive_path, "/tmp/{}".format(fil))
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
    except Exception:
        return False
    return True
