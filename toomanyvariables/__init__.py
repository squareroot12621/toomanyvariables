"""Too Many Variables! is an esoteric programming language.
For more information, see the README.md at
<link>.
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
