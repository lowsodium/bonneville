# -*- coding: utf-8 -*-
'''
    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2013 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.


    bonneville.syspaths
    ~~~~~~~~~~~~~

    Salt's defaults system paths
'''

# Import python libs
import sys
import os.path

try:
    # Let's try loading the system paths from the generated module at
    # installation time.
    from bonneville._syspaths import (  # pylint: disable=E0611
        ROOT_DIR,                 # because pylint thinks that _syspaths is an
        CONFIG_DIR,               # attribute of bonneville.__init__
        CACHE_DIR,
        SOCK_DIR,
        SRV_ROOT_DIR,
        BASE_FILE_ROOTS_DIR,
        BASE_PILLAR_ROOTS_DIR,
        BASE_MASTER_ROOTS_DIR,
        LOGS_DIR,
        PIDFILE_DIR,
    )
except ImportError:
    # The installation time was not generated, let's define the default values
    if sys.platform.startswith('win'):
        ROOT_DIR = r'c:\salt' or '/'
        CONFIG_DIR = os.path.join(ROOT_DIR, 'conf')
    else:
        ROOT_DIR = '/'
        CONFIG_DIR = os.path.join(ROOT_DIR, 'etc', 'bonneville')
    CACHE_DIR = os.path.join(ROOT_DIR, 'var', 'cache', 'bonneville')
    SOCK_DIR = os.path.join(ROOT_DIR, 'var', 'run', 'bonneville')
    SRV_ROOT_DIR = os.path.join(ROOT_DIR, 'srv')
    BASE_FILE_ROOTS_DIR = os.path.join(SRV_ROOT_DIR, 'bonneville')
    BASE_PILLAR_ROOTS_DIR = os.path.join(SRV_ROOT_DIR, 'pillar')
    BASE_MASTER_ROOTS_DIR = os.path.join(SRV_ROOT_DIR, 'bonneville-master')
    LOGS_DIR = os.path.join(ROOT_DIR, 'var', 'log', 'bonneville')
    PIDFILE_DIR = os.path.join(ROOT_DIR, 'var', 'run')
