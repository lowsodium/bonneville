# -*- coding: utf-8 -*-
'''
Modules used to control the master itself
'''

import os
# Import bonneville libs
from bonneville import syspaths
import bonneville.config
import bonneville.loader
import bonneville.payload
import bonneville.utils
import bonneville.exceptions


class Wheel(object):
    '''
    ``WheelClient`` is an interface to Salt's :ref:`wheel modules
    <all-bonneville.wheel>`. Wheel modules interact with various parts of the Salt
    Master.

    Importing and using ``WheelClient`` must be done on the same machine as the
    Salt Master and it must be done using the same user that the Salt Master is
    running as.
    '''
    def __init__(self, opts=None):
        if not opts:
            opts = bonneville.config.client_config(
                    os.environ.get(
                        'SALT_MASTER_CONFIG',
                        os.path.join(syspaths.CONFIG_DIR, 'master')
                        )
                    )

        self.opts = opts
        self.w_funcs = bonneville.loader.wheels(opts)

    def get_docs(self):
        '''
        Return a dictionary of functions and the inline documentation for each
        '''
        ret = [(fun, self.w_funcs[fun].__doc__)
                for fun in sorted(self.w_funcs)]

        return dict(ret)

    def call_func(self, fun, **kwargs):
        '''
        Execute a master control function
        '''
        if fun not in self.w_funcs:
            return 'Unknown wheel function'
        f_call = bonneville.utils.format_call(self.w_funcs[fun], kwargs)
        return self.w_funcs[fun](*f_call.get('args', ()), **f_call.get('kwargs', {}))

    def master_call(self, **kwargs):
        '''
        Send a function call to a wheel module through the master network interface
        Expects that one of the kwargs is key 'fun' whose value is the namestring
        of the function to call
        '''
        load = kwargs
        load['cmd'] = 'wheel'
        sreq = bonneville.payload.SREQ(
                'tcp://{0[interface]}:{0[ret_port]}'.format(self.opts),
                )
        ret = sreq.send('clear', load)
        if ret == '':
            raise bonneville.exceptions.EauthAuthenticationError
        return ret
