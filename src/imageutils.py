#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

class Resizer(object):

    def __init__(self, path):
        self.image = Image.open(path)
        image_size = self.image.size
        self.flip = image_size[0] < image_size[1]


    def resize(self, outpath, size):
        print outpath
        # flip size in case the image is rotated
        if self.flip:
            size = size[1], size[0]
        resized = self.image.resize(size, Image.ANTIALIAS)
        resized.save(outpath)
