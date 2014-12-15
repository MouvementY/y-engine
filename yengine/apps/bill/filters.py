"""
Filters are here to ensure a quality of the signatures being displayed
and avoid point-based signatures or blank canvas
"""

import re
import io
import base64

from PIL import Image


class ImageConvertor(object):

    DATA_PATTERN = re.compile(r'base64,(.*)')

    def _extract_data_from_uri(self, data_uri):
        matches = re.search(self.DATA_PATTERN, data_uri)
        if matches is None:
            raise ValueError("The base64 format has been broken")
        data = matches.group(1)
        return data

    def image_from_data_uri(self, data_uri):
        data = self._extract_data_from_uri(data_uri)
        if data is None:
            return None
        return self.image_from_data(data)

    def image_from_data(self, data):
        stream = io.BytesIO(base64.b64decode(data))
        image = Image.open(stream)
        return image


class DotSignatureIdentifierProcessor(object):
    threshold = 0

    def __init__(self, threshold=0.01):
        self.threshold = threshold

    def get_colored_pixel_count(self, image):
        count = 0
        width, height = image.size

        pixels = image.load()
        for i in range(width):
            for j in range(height):
                p = pixels[i, j]

                # check the alpha component
                if p[3] > 0:
                    count += 1

        return count

    def get_colored_pixel_ratio(self, image):
        count = self.get_colored_pixel_count(image)
        width, height = image.size
        total = width * height
        return count / total

    def process(self, image):
        ratio = self.get_colored_pixel_ratio(image)
        if ratio < self.threshold:
            return None
        return image
