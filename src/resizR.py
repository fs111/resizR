#!/usr/bin/env python

import pyinotify
import os
import os.path
import user
import imageutils
import user

BASEPATH = os.path.join(user.home, "resizR")

SIZES = ((800, 600), (1024, 768), (1280, 1024), (1600, 1200))


class ImageEventHandler(pyinotify.ProcessEvent):

    def my_init(self):
        self.path = BASEPATH
        self._incoming = {}
        self._prepareDirectories()

    def process_default(self, event):
        if event.mask == pyinotify.IN_CREATE:
            self._handleIncoming(event)
        elif event.mask == pyinotify.IN_CLOSE_WRITE:
            self._handleFileComplete(event)

    def _handleFileComplete(self, event):
        if event.pathname in self._incoming:
            self.resize(event)
            del self._incoming[event.pathname]

    
    def _handleIncoming(self, event):
        if not event.dir:
            self._incoming[event.pathname] = event
 

    def resize(self, event):
        if not event.dir:
            def run():
                fullpath = event.pathname
                fname = os.path.basename(fullpath)
                resizer = imageutils.Resizer(fullpath)
                for size in SIZES:
                        outpath = os.path.join(event.path,
                             directory_for_size(size),
                             fname)
                        resizer.resize(outpath, size)


    def _prepareDirectories(self):
        for size in SIZES:
            dir = os.path.join(self.path, directory_for_size(size))
            if not (os.path.isdir(dir)):
                os.makedirs(dir)


def directory_for_size(fmt_tuple):
    return "%sx%s" % (fmt_tuple[0], fmt_tuple[1])


def main():
    handler = ImageEventHandler()
    mgr = pyinotify.WatchManager()
    mgr.add_watch(BASEPATH, pyinotify.ALL_EVENTS)
    notifier = pyinotify.Notifier(mgr, handler)
    notifier.loop()


if __name__ == "__main__":
    main()
