#!/usr/bin/python3
'''
Fabric script that distributes an archive to your web servers
'''
import os.path
from fabric.api import *

env.hosts = ['66.70.184.246', '34.229.226.224']


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
