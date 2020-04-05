# -*- coding: utf-8 -*-
'''
Generate the salt thin tarball from the installed python files
'''

# Import python libs
import os
import tarfile

# Import third party libs
import jinja2
import yaml
try:
    import markupsafe
    HAS_MARKUPSAFE = True
except ImportError:
    # Older jinja does not need markupsafe
    HAS_MARKUPSAFE = False

# Import bonneville libs
import bonneville
import bonneville.utils

SALTCALL = '''
from bonneville.scripts import bonneville_call
if __name__ == '__main__':
    salt_call()
'''


def gen_thin(cachedir):
    '''
    Generate a salt-thin tarball and load it into the location in the cachedir
    '''
    thindir = os.path.join(cachedir, 'thin')
    if not os.path.isdir(thindir):
        os.makedirs(thindir)
    thintar = os.path.join(thindir, 'thin.tgz')
    thinver = os.path.join(thindir, 'version')
    salt_call = os.path.join(thindir, 'salt-call')
    with open(salt_call, 'w+') as fp_:
        fp_.write(SALTCALL)
    if os.path.isfile(thintar):
        if not os.path.isfile(thinver):
            os.remove(thintar)
        elif open(thinver).read() == bonneville.__version__:
            return thintar
    tops = [
            os.path.dirname(bonneville.__file__),
            os.path.dirname(jinja2.__file__),
            os.path.dirname(yaml.__file__),
            ]
    if HAS_MARKUPSAFE:
        tops.append(os.path.dirname(markupsafe.__file__))
    tfp = tarfile.open(thintar, 'w:gz', dereference=True)
    start_dir = os.getcwd()
    for top in tops:
        base = os.path.basename(top)
        os.chdir(os.path.dirname(top))
        for root, dirs, files in os.walk(base):
            for name in files:
                if not name.endswith(('.pyc', '.pyo')):
                    tfp.add(os.path.join(root, name))
    os.chdir(thindir)
    tfp.add('salt-call')
    with open(thinver, 'w+') as fp_:
        fp_.write(bonneville.__version__)
    os.chdir(os.path.dirname(thinver))
    tfp.add('version')
    os.chdir(start_dir)
    tfp.close()
    return thintar


def thin_sum(cachedir, form='sha1'):
    '''
    Return the checksum of the current thin tarball
    '''
    thintar = gen_thin(cachedir)
    return bonneville.utils.get_hash(thintar, form)
