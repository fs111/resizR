#!/usr/bin/env python
# -*- coding: utf-8 
"""
configuration module for resizR.

author: André Kelpe <efeshundertelf at googlemail dot com>
license: GPLv3
"""
import user
import os.path
import sys

# here we store our config
_CONFIG_DIR = os.path.join(user.home, ".resizR")
_CONFIG_FILE = os.path.join(_CONFIG_DIR, "resizRconfig.py")
# use python as the config file, if somebody puts problematic code in there, that
# is their problem.
_CFG_TEMPLATE = """
#!/usr/bin/env python
# -*- coding: utf-8 
# this is where we store stuff
BASEPATH = "~/resizR"

# cleans up the directory every time resizR starts
CLEAN_ON_START = False

# we will create these sizes
SIZES = ((800, 600), (1024, 768), (1280, 1024), (1600, 1200))
"""
# first make sure the directory and file are present
if not os.path.exists(_CONFIG_FILE):
    if not os.path.isdir(_CONFIG_DIR):
        os.makedirs(_CONFIG_DIR)
    cfg = open(_CONFIG_FILE, "w")
    cfg.write(_CFG_TEMPLATE)
    cfg.close()

# now a simple import trick
sys.path.insert(0, _CONFIG_DIR)
import resizRconfig as USERCONFIG
# and finally replace things like ~ for convinience of the user
USERCONFIG.BASEPATH = os.path.expanduser(USERCONFIG.BASEPATH)

