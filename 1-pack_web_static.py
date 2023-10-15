#!/usr/bin/python3
"""
A fabric script to genereate tgz archive
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
