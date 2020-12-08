#!/usr/bin/env python

import os, fnmatch


py_root = os.environ.get('pythonLocation', '')

if not py_root:
    py_root = '/opt/hostedtoolcache'


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


rc_path = find('*.rc.github.release', py_root)

if rc_path != []:
    print(rc_path[0])
