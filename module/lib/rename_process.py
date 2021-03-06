from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import sys


def renameProcess(new_name):
    """ Renames the process calling the function to the given name. """
    if sys.platform != 'linux2':
        return False
    try:
        from ctypes import CDLL
        libc = CDLL('libc.so.6')
        libc.prctl(15, new_name, 0, 0, 0)
        return True
    except Exception as e:
        #print "Rename process failed", e
        return False
