#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Template for building command line applications
"""
__author__  = "Mark Butterworth"
__version__ = "0.01 (May 2020)"
__license__ = "MIT"

# Ver 0.01 0720  Initial version

# Copyright 2020 Mark Butterworth
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import sys
import argparse

DEBUG = 0
VERBOSE = False


###############################################################################

def cli():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.version = __version__
    parser.add_argument('-V', '--version', action='version')
    parser.add_argument('-D', '--debug', action='count',
        help='Increase debug level, e.g. -DDD = level 3.')
    parser.add_argument('-v', '--verbose', action='store_true')
    # nargs = ? for optional or + for one or more
    parser.add_argument('filename', type=str, nargs='*', default='-',
        help='Path to file.  Defaults to stdin.')

    args = parser.parse_args()
    global DEBUG, VERBOSE
    if args.debug:
        DEBUG = args.debug
        print(f'DEBUG LEVEL:{args.debug}')
        print('Arguments:', args)

    VERBOSE = args.verbose




    return 0

if __name__=='__main__':
    retcode = cli()
    exit(retcode)
