#!/usr/bin/env python
__author__ = 'Laurence Armstrong'
authorship_string = "%s created on %s by %s (%d)\n%s\n" % \
                    ("singleton.py", "9/04/15", __author__, 15062061, "-----" * 15) \
    if __name__ == '__main__' else ""
print(authorship_string, end="")


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]