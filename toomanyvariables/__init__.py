# MIT License
#
# Copyright (c) 2024 squareroot12621
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# This code has been modified from code, made by squareroot12621, under
# the Creative Commons Zero v1.0 Universal license. The original code
# can be located at
# https://github.com/squareroot12621/messenger-language/blob/main/messenger/__init__.py .

"""Too Many Variables! is an esoteric programming language.
For more information, see the README.md at
https://github.com/squareroot12621/toomanyvariables/blob/main/README.md .
"""

import argparse
import sys
from toomanyvariables.interpreter import *

if __name__ == '__main__': # Run directly
    parser = argparse.ArgumentParser(
        prog='Too Many Variables! Interpreter v1.0',
        description='Runs Too Many Variables! (TMV), a programming language '
                    'all about assigning variables.',
        formatter_class=lambda prog: argparse.HelpFormatter(
                                         prog, max_help_position=30
                                     )
    )
    parser.add_argument('code',
                        help='the TMV code to be run',
                        type=str)
    parser.add_argument('-c', '--check',
                        help='show code and flags before running code',
                        action='store_true')
    arguments = parser.parse_args(args=None if sys.argv[1:] else ['-h'])
    
    code = arguments.code
    if arguments.check:
        print( '\n'
               'Code:\n'
              f'{code}\n'
               '\n'
               'Flags:\n'
               'None.\n')
        codeChecked = input('Type "no" (without quotes) to cancel execution.\n'
                            'Type anything else to continue.\n')
        if codeChecked.upper() != 'NO':
            run_TMV(parse_TMV(code))
    else:
        run_TMV(parse_TMV(code))
