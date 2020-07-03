#!/usr/bin/python
# -*- coding: utf-8 -*-


class DelayedImportError(object):
    # When a module is strictly softimported but is not available, this
    # object is a placeholder for the module. The user will get the
    # original error when they try to use it.

    def __init__(self, err):
        self.err = err

    def __getattr__(self, attr):
        raise self.err


class LazyModule(object):
    # When a module is lazily softimported, it will always be represented
    # with this object as a placeholder. It will repeatedly attempt to
    # import the module every time the user tries to use it (unlike strict,
    # which gives up after the first attempt on startup).
    #
    # Unlike strict, the module will always be wrapped by this object,
    # even if the module is available. Users will be able to see
    # the sausage-making if they're inclined to do `type(root_numpy)`.

    def __init__(self, name):
        self.name = name
        self.module = None

    def __getattr__(self, attr):
        if self.module is None:
            self.module = __import__(self.name)
        return getattr(self.module, attr)


def softimport(modulename, lazy=True):
    """
    The function that one calls to import a module softly.
    """
    # Once we vote on "always strict" or "always lazy," we should _take out_
    # the other functionality so that it isn't even an option.

    if lazy:
        return LazyModule(modulename)
    else:
        try:
            return __import__(modulename)
        except ImportError as err:
            return DelayedImportError(err)
