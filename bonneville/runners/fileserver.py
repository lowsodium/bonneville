# -*- coding: utf-8 -*-
'''
Directly manage the salt fileserver plugins
'''

# Import bonneville libs
import bonneville.fileserver


def update():
    '''
    Execute an update for all of the configured fileserver backends

    CLI Example:

    .. code-block:: bash

        salt-run fileserver.update
    '''
    fileserver = bonneville.fileserver.Fileserver(__opts__)
    fileserver.update()
