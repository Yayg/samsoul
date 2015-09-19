import cmd

class SamsoulCmd(cmd.Cmd):

    ns = None

    prompt = 'samsoul> '
    intro = "Samsoul interactive console\n"

    doc_header = 'Commands'
    undoc_header = ''

    def __init__(self, ns):
        super().__init__()
        self.ns = ns


    def do_list_users(self, line):
        print('hello')

    def do_info(self, line):
        for d in self.ns.data:
            print(str(d).ljust(15) + str(self.ns.data[d]).rjust(50))
        print()

    def do_EOF(self, line):
        print()
        return True
