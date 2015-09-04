#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   Author  :   evilbinary
#   E-mail  :   rootntsd@gmail.com
#   Date    :   15/9/5 12:21:19
#   Desc    :
import os
import sys

if __name__ == "__main__":
    # GETTING-STARTED: change 'myproject' to your project name:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cl.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
