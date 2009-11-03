#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utilities for working with images for resizR"""

from PIL import Image

class Resizer(object):
    """Simple class that uses the fine PIL library to resizes images"""

    def __init__(self, path):
        self.image = Image.open(path)
        image_size = self.image.size
        # in case the images is 1200x1600 and not 1600x1200 we have to 
        # know that so that we do not create lots of fat looking people 
        # in the resized images :)
        self.flip = image_size[0] < image_size[1]


    def resize(self, outpath, size):
        if self.flip:
            size = size[1], size[0]
        resized = self.image.resize(size, Image.ANTIALIAS)
        resized.save(outpath)
