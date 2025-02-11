# All items are dynamically added by classes in operator.py
# This module acts as a container of BinaryOp instances
_delayed = {}
_delayed_commutes_to = {
    "absfirst": "abssecond",
    "abssecond": "absfirst",
    "floordiv": "rfloordiv",
    "rfloordiv": "floordiv",
}
from grblas import operator  # noqa isort:skip
from . import numpy  # noqa isort:skip

del operator


def __getattr__(key):
    if key in _delayed:
        func, kwargs = _delayed.pop(key)
        rv = func(**kwargs)
        globals()[key] = rv
        if key in _delayed_commutes_to:
            other_key = _delayed_commutes_to[key]
            if other_key in globals():
                other = globals()[other_key]
            else:
                other = __getattr__(other_key)
            rv.commutes_to = other
        return rv
    raise AttributeError(f"module {__name__!r} has no attribute {key!r}")
