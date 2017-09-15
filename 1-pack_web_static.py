#!/usr/bin/python3
'''
script that generates a .tgz archive from the contents of the web_static
'''
from fabric.api import *
import time


def do_pack():
    time_for_name = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time_for_name))
        return ("versions/web_static_{}.tgz".format(time_for_name))
    except:
        return None
