#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup 

setup (name = 'resizR', 
       description = "resizR is a pyinotify PIL hack to resize images automatically", 
       author = "André Kelpe", 
       author_email = "efeshundertelf@googlemail.com", 
       version = '0.2', 
       packages = ['resizRmodules',],
       scripts = ["src/resizR"],
       url = "http://github.com/fs111/resizR",
       package_dir = {'': 'src'}
       )

