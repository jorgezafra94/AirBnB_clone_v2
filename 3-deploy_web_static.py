#!/usr/bin/python3
""" using fabric and create a tar file .tgz
"""
from datetime import datetime
from fabric.api import *
import os
import shlex
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['35.227.82.74', '35.231.166.249']
env.user = 'ubuntu'


def deploy():
    path = do_pack()
    if not path:
        return (False)
    result = do_deploy(path)
    return (result)
