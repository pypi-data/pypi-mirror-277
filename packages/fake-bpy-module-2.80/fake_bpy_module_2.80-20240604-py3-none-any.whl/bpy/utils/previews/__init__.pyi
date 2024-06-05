"""
This module contains utility functions to handle custom previews.

It behaves as a high-level 'cached' previews manager.

This allows scripts to generate their own previews, and use them as icons in UI widgets
('icon_value' for UILayout functions).


--------------------

```__/__/__/release/scripts/templates_py/ui_previews_custom_icon.py```

"""

import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ImagePreviewCollection:
    """Dictionary-like class of previews.This is a subclass of Python's built-in dict type,
    used to store multiple image previews.
    """

    def clear(self):
        """Clear all previews."""
        ...

    def close(self):
        """Close the collection and clear all previews."""
        ...

    def copy(self):
        """D.copy() -> a shallow copy of D"""
        ...

    def fromkeys(self):
        """Create a new dictionary with keys from iterable and values set to value."""
        ...

    def get(self, key, default=None):
        """Return the value for key if key is in the dictionary, else default.

        :param key:
        :param default:
        """
        ...

    def items(self):
        """D.items() -> a set-like object providing a view on D's items"""
        ...

    def keys(self):
        """D.keys() -> a set-like object providing a view on D's keys"""
        ...

    def load(
        self, name: str | None, path, path_type, force_reload: bool | None = False
    ) -> bpy.types.ImagePreview:
        """Generate a new preview from given file path, or return existing one matching name.

        :param name: The name (unique id) identifying the preview.
        :type name: str | None
        :param path:
        :param path_type:
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :type force_reload: bool | None
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """
        ...

    def new(self, name: str | None) -> bpy.types.ImagePreview:
        """Generate a new empty preview, or return existing one matching name.

        :param name: The name (unique id) identifying the preview.
        :type name: str | None
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """
        ...

    def pop(self):
        """D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
        If key is not found, d is returned if given, otherwise KeyError is raised

        """
        ...

    def popitem(self):
        """D.popitem() -> (k, v), remove and return some (key, value) pair as a
        2-tuple; but raise KeyError if D is empty.

        """
        ...

    def setdefault(self, key, default=None):
        """Insert key with a value of default if key is not in the dictionary.Return the value for key if key is in the dictionary, else default.

        :param key:
        :param default:
        """
        ...

    def update(self):
        """D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
        If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
        If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
        In either case, this is followed by: for k in F:  D[k] = F[k]

        """
        ...

    def values(self):
        """D.values() -> an object providing a view on D's values"""
        ...

def new() -> ImagePreviewCollection:
    """

    :return: a new preview collection.
    :rtype: ImagePreviewCollection
    """

    ...

def new() -> ImagePreviewCollection:
    """

    :return: a new preview collection.
    :rtype: ImagePreviewCollection
    """

    ...

def remove(pcoll: ImagePreviewCollection | None):
    """Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    :type pcoll: ImagePreviewCollection | None
    """

    ...

def remove(pcoll: ImagePreviewCollection | None):
    """Remove the specified previews collection.

    :param pcoll: Preview collection to close.
    :type pcoll: ImagePreviewCollection | None
    """

    ...
