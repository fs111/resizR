#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""resizR is a pyinotify PIL hack to resize images automatically

author: André Kelpe <efeshundertelf at googlemail dot com>
license: GPLv3
"""
import pyinotify
import os
import os.path
import user
import imageutils
import user

# this is where we store stuff
BASEPATH = os.path.join(user.home, "resizR")

# we will create these sizes
SIZES = ((800, 600), (1024, 768), (1280, 1024), (1600, 1200))


class ImageEventHandler(pyinotify.ProcessEvent):
    """Eventhandler for the directory we are monitoring. The class
    does state tracking: 
    Everytime a new file is created we will receive a pyinotify.IN_CREATE event. Since that
    is fired when the file is created and not when it is fully written to disk, it will
    be stored in an internal dictionary and will be reinspected as soon as we receive the
    IN_CLOSE_WRITE event for the same file. This makes sure we only pass fully written files
    to the resizing done by PIL.
    """

    def my_init(self):
        """overwritten method from the pyinotify framework. __init__ cannot
        be overwritten according to the docs, so this is the way to initialize our own
        stuff"""
        self.path = BASEPATH
        
        self._incoming = {}
        self._prepareDirectories()

    def process_default(self, event):
        """Handles all inotify events, but only reacts on two of them"""
        if event.mask == pyinotify.IN_CREATE:
            self._handleIncoming(event)
        elif event.mask == pyinotify.IN_CLOSE_WRITE:
            self._handleFileComplete(event)

    def _handleFileComplete(self, event):
        """When the file has been closed, we can start processing it, but only if
        it is a new file."""
        # make sure we have seen this before
        if event.pathname in self._incoming:
            self._resize(event)
            # finally remove the event from our state tracking dict
            del self._incoming[event.pathname]

    
    def _handleIncoming(self, event):
        """handles new incoming files"""
        if not event.dir:
            self._incoming[event.pathname] = event
 

    def _resize(self, event):
        fullpath = event.pathname
        fname = os.path.basename(fullpath)
        resizer = imageutils.Resizer(fullpath)
        for size in SIZES:
                outpath = os.path.join(event.path,
                     directory_for_size(size),
                     fname)
                resizer.resize(outpath, size)


    def _prepareDirectories(self):
        """This method creates the resizR and all its subdirectories """
        for size in SIZES:
            dir = os.path.join(self.path, directory_for_size(size))
            if not (os.path.isdir(dir)):
                os.makedirs(dir)


def directory_for_size(fmt_tuple):
    """small helper method that returns directory names for sizes.
    (800, 600) will become "800x600"
    """
    return "%sx%s" % (fmt_tuple[0], fmt_tuple[1])


def main():
    """Yes, this is a main method, you guessed it right"""
    handler = ImageEventHandler()
    mgr = pyinotify.WatchManager()
    mgr.add_watch(BASEPATH, pyinotify.ALL_EVENTS)
    notifier = pyinotify.Notifier(mgr, handler)
    notifier.loop()


if __name__ == "__main__":
    main()
