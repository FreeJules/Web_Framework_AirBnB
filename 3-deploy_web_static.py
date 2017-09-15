#!/usr/bin/python3
'''
creates and distributes an archive to your web servers
'''
from fabric.api import *
import time
import os.path

env.hosts = ['66.70.184.246', '34.229.226.224']


def do_pack():
    """pack"""
    time_for_name = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_for_name))
        return ("versions/web_static_{}.tgz".format(time_for_name))
    except:
        return None


def do_deploy(archive_path):
    """do deploy"""
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        tmp_path = "/tmp/" + archive_path.split("/")[1]
        data_path = "/data/web_static/releases/" + \
                    archive_path.split("/")[1][:-4] + "/"
        put(archive_path,  tmp_path)
        run("mkdir -p " + data_path)
        run("tar -xzf " + tmp_path + " -C " + data_path)
        run("rm " + tmp_path)
        run("mv " + data_path + "web_static/* " + data_path)
        run("rm -rf " + data_path + "web_static")
        run("rm -rf /data/web_static/current")
        run("ln -s " + data_path + " /data/web_static/current")
        return True
    except:
        return False


def deploy():
    path = do_pack()
    return do_deploy(path)
