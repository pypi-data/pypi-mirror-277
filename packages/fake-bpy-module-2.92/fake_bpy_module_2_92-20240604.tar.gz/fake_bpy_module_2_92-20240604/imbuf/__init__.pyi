"""
This module provides access to Blender's image manipulation API.

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def load(filepath: str):
    """Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: str
    :return: the newly loaded image.
    """

    ...

def new(size):
    """Load a new image.

    :param size: The size of the image in pixels.
    :return: the newly loaded image.
    """

    ...

def write(image, filepath: str):
    """Write an image.

    :param image: the image to write.
    :param filepath: the filepath of the image.
    :type filepath: str
    """

    ...
