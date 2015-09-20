import cmd
from texttable import Texttable
from prettytable import PrettyTable

class SamsoulCmd(cmd.Cmd):

    prompt = 'samsoul> '
    intro = "Samsoul interactive console\n"

    doc_header = 'Commands'

    def __init__(self, protocol):
        super().__init__()
        self.protocol = protocol


    def do_list_users(self, line):
        """list_users [<exp>]
        List all users or each one matching the exp given in any of the rows
        """
        users = self.protocol.cmd_list_users(exp=line, return_list=True)
        t = PrettyTable(users[0])
        for u in users[1:]:
            t.add_row(u)
        print(t)

    def do_info(self, line):
        for d in self.protocol.hello_data:
            print(str(d).ljust(15) +
                    str(self.protocol.hello_data[d].decode("utf-8")).rjust(50))
        print()

    def do_say(self, line):
        """say [<something>]
        Repeat after me"""
        if line != '':
            print(line)

    def do_EOF(self, line):
        print()
        return True
