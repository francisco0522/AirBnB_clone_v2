#!/usr/bin/python3
"generates a .tgz archive from the contents of the web_static"
from fabric.api import local, put, run, env
from datetime import datetime
from os.path import isfile

env.hosts = ["35.243.229.224", "34.229.175.198"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if isfile(archive_path) is False:
        return False
    try:
        put(archive_path, '/tmp/')
        name_file_ext = archive_path.split("/")[1]
        name_file = name_file_ext.split(".")[0]
        cmd_mkdir = 'mkdir -p /data/web_static/releases/{}'.format(name_file)
        run(cmd_mkdir)
        cmd_uncom = 'tar -xzf /tmp/{}'.format(name_file_ext)
        cmd_uncom += ' -C /data/web_static/releases/{}'.format(name_file)
        run(cmd_uncom)
        cmd_rm_file = 'rm /tmp/{}'.format(name_file_ext)
        run(cmd_rm_file)
        cmd_mv = 'mv /data/web_static/releases/'
        cmd_mv += '{}/web_static/*'.format(name_file)
        cmd_mv += ' /data/web_static/releases/{}/'.format(name_file)
        run(cmd_mv)
        cmd_rm_dir = 'rm -rf /data/web_static/releases/{}'.format(name_file)
        cmd_rm_dir += '/web_static'
        run(cmd_rm_dir)
        run('rm -rf /data/web_static/current')
        cmd_cre_sym = 'ln -s /data/web_static/releases/{}/'.format(name_file)
        cmd_cre_sym += ' /data/web_static/current'
        run(cmd_cre_sym)
        print("New version deployed!")
        return True
    except Exception:
        return False
