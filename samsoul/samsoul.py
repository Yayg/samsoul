#! /usr/bin/env python3.4

"""
Usage:
    samsoul [-si]
    samsoul -u [<login>]
    samsoul --generate-conf

Options:
    -s                  Start netsoul deamon
    -i                  Launch interactive session
    --generate-conf     Generate a conf from actual PIE network mapping
    -u                  List users or get specific user informations
"""

import sys
import socket
import docopt
import pprint
import os

import samsoul
from .conf import *
from .protocol import *
from .logging import *
from .cmd import *

# Using pprint instead of basic print
print = pprint.pprint

def run():
    args = docopt.docopt(__doc__)

    config = None

    # Configuration options
    if args['--generate-conf']:
        generate_conf()
        return
    else:
        config_file = None
        try:
            config_file = open(os.path.expanduser('~') + '/.samsoulrc').read()
        except BaseException as err:
            logging().error(2,
                """Missing config file. Use --generate-conf and create
                ~/.samsoulrc file""")
            sys.exit(1)
        config = get_conf(config_file)

    protocol = Protocol(config)

    # Netsoul deamon
    if args['-s']:
        print(protocol.data)
    # Netsoul commands
    elif args['-u']:
        if args['<login>']:
            raise NotImplementedError
        else:
            raise NotImplementedError
    elif args['-i']:
        while True:
            try:
                SamsoulCmd(protocol).cmdloop()
                break
            except KeyboardInterrupt:
                print("Hey it hurts, please use Ctrl+D to escape.")


if __name__ == '__main__':
    run()
