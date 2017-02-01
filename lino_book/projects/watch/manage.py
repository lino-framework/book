#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    import os
    from django.core.management import execute_from_command_line

    os.environ["DJANGO_SETTINGS_MODULE"] = "lino_book.projects.watch.settings"
    execute_from_command_line(sys.argv)
