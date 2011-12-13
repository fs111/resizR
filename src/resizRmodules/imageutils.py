#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utilities for working with images for resizR"""

from PIL import Image

class Resizer(object):
    """Simple class that uses the fine PIL library to resizes images"""

    def __init__(self, path):
        """Constructs a new Resizer object with the given
        path, which can then be used to resize and image."""

        self.image = Image.open(path)
        image_size = self.image.size
        # in case the images is 1200x1600 and not 1600x1200 we have to 
        # know that so that we do not create lots of fat looking people 
        # in the resized images :)
        self.flip = image_size[0] < image_size[1]


    def resize(self, outpath, size):
        """Resizes the image given in the constructor to the given size
        argument and saves it at the given location"""
        if isinstance(size, str):
            size = size.replace("%", "")
            factor = float("0." + size)
            size = (int(self.image.size[0] * factor),
                    int(self.image.size[1] * factor))
        elif self.flip:
            size = size[1], size[0]
        resized = self.image.resize(size, Image.ANTIALIAS)
        resized.save(outpath)
