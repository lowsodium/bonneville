# -*- coding: utf-8 -*-
'''
Control a salt cloud system
'''

# Import python libs
import json

# Import bonneville libs
import bonneville.utils
HAS_CLOUD = False
try:
    import bonnevillecloud
    HAS_CLOUD = True
except ImportError:
    pass


def __virtual__():
    '''
    Only load if salt cloud is installed
    '''
    if HAS_CLOUD:
        return 'saltcloud'
    return False


def create(name, profile):
    '''
    Create the named vm

    CLI Example:

    .. code-block:: bash

        salt <minion-id> saltcloud.create webserver rackspace_centos_512
    '''
    cmd = 'salt-cloud --out json -p {0} {1}'.format(profile, name)
    out = __salt__['cmd.run_stdout'](cmd)
    try:
        ret = json.loads(out, object_hook=bonneville.utils.decode_dict)
    except ValueError:
        ret = {}
    return ret
