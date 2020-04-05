# -*- coding: utf-8 -*-
'''
This module contains the function calls to execute command line scipts
'''

# Import python libs
import os
import sys

# Import bonneville libs
import bonneville
import bonneville.cli


def bonneville_master():
    '''
    Start the bonneville-master.
    '''
    master = bonneville.Master()
    master.start()


def bonneville_minion():
    '''
    Kick off a bonneville minion daemon.
    '''
    if '' in sys.path:
        sys.path.remove('')
    minion = bonneville.Minion()
    minion.start()


def bonneville_syndic():
    '''
    Kick off a bonneville syndic daemon.
    '''
    pid = os.getpid()
    try:
        syndic = bonneville.Syndic()
        syndic.start()
    except KeyboardInterrupt:
        os.kill(pid, 15)


def bonneville_key():
    '''
    Manage the authentication keys with bonneville-key.
    '''
    try:
        bonnkey = bonneville.cli.SaltKey()
        bonnkey.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')


def bonneville_cp():
    '''
    Publish commands to the bonneville system from the command line on the
    master.
    '''
    try:
        cp_ = bonneville.cli.SaltCP()
        cp_.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')


def bonneville_call():
    '''
    Directly call a bonneville command in the modules, does not require a
    running bonneville minion to run.
    '''
    if '' in sys.path:
        sys.path.remove('')
    try:
        client = bonneville.cli.SaltCall()
        client.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')


def bonneville_run():
    '''
    Execute a bonneville convenience routine.
    '''
    if '' in sys.path:
        sys.path.remove('')
    try:
        client = bonneville.cli.SaltRun()
        client.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')


def bonneville_ssh():
    '''
    Execute the bonneville-ssh system
    '''
    if '' in sys.path:
        sys.path.remove('')
    try:
        client = bonneville.cli.SaltSSH()
        client.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')


def bonneville_main():
    '''
    Publish commands to the bonneville system from the command line on the
    master.
    '''
    if '' in sys.path:
        sys.path.remove('')
    try:
        client = bonneville.cli.SaltCMD()
        client.run()
    except KeyboardInterrupt:
        raise SystemExit('\nExiting gracefully on Ctrl-c')
