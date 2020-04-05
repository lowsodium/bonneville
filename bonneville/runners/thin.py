# -*- coding: utf-8 -*-
'''
The thin runner is used to manage the salt thin systems.

Salt Thin is a transport-less version of Salt that can be used to run rouitines
in a standalone way. This runner has tools which generate the standalone salt
system for easy consumption.
'''

# Import python libs
from __future__ import print_function

# Import Salt libs
import bonneville.utils.thin


def generate():
    '''
    Generate the salt-thin tarball and print the location of the tarball
    '''
    print(bonneville.utils.thin.gen_thin(__opts__['cachedir']))
