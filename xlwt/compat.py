import sys

PY3 = sys.version_info[0] >= 3

if PY3:
    unicode_type = str
    basestring = str
    int_types = (int,)
    long = int

else:
    # Python 2
    unicode_type = unicode
    basestring = basestring
    int_types = (int, long)
    long = long
