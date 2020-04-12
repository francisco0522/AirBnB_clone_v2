#!/usr/bin/python3
# This fabscript deploys the web static content
from os import path
from fabric.api import sudo, env, put, local
from datetime import datetime

env.hosts = ["35.243.229.224", "34.229.175.198"]


def do_pack():
        now = datetime.utcnow()
        file_ = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                              now.month,
                                                              now.day,
                                                              now.hour,
                                                              now.minute,
                                                              now.second)

        if not path.isdir("versions"):
                if local("mkdir -p versions").failed:
                        return None
        if local('tar -cvzf {} web_static'.format(file_)).failed:
                return None
        return file_


def do_deploy(archive_path):
    """
    send and configure the web static content
    """
    # Assure that given parameter is a file
    if not path.isfile(archive_path):
            return False
    file_ = archive_path.split("/")[-1]
    name = file_.split(".")[0]
    tmp = "/tmp/{}".format(file_)
    data = "/data/web_static/releases/{}/".format(name)
    current = "/data/web_static/current"
    if put("0-setup_web_static.sh", "/tmp/").failed:
            return False
    if sudo("chmod u+x /tmp/0-setup_web_static.sh").failed:
            return False
    if sudo("/tmp/0-setup_web_static.sh").failed:
            return False
    if sudo("rm /tmp/0-setup_web_static.sh").failed:
            return False
    if put(archive_path, tmp).failed:
            return False
    if sudo("rm -rf {}".format(data)).failed:
            return False
    if sudo("mkdir -p {}".format(data)).failed:
            return False
    if sudo("tar -xzf {} -C {}".format(tmp, data)).failed:
            return False
    if sudo("rm {}".format(tmp)).failed:
            return False
    if sudo("mv {}web_static/* {}".format(data, data)).failed:
            return False
    if sudo("rm -rf {}web_static".format(data)).failed:
            return False
    if sudo("rm -rf {}".format(current)).failed:
            return False
    if sudo("ln -s {} {}".format(data, current)).failed:
            return False
    print("New version deployed!")

    return True


def deploy():
    """
    This function do a full deployment
    """
    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
