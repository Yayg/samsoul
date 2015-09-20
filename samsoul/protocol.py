import socket
import copy
import time

class Protocol:
    hello_data = dict() # NetSoul personal data
    ns_server = 'ns-server.epita.fr'
    ns_port = 4242

    def __init__(self, conf):
        self.connect()
        self.conf = conf

    def get_data(self, hello):
        s = hello.split()
        self.hello_data["socket"] = s[1]
        self.hello_data["md5"] = s[2]
        self.hello_data["ip"] = s[3]
        self.hello_data["port"] = s[4]
        self.hello_data["timestamp"] = s[5]

    def connect(self):
        ns = socket.socket()
        ns.connect((socket.gethostbyname(self.ns_server), self.ns_port))
        hello = ns.recv(8192)
        self.get_data(hello)
        self.ns_socket = ns

    def send_command(self, command):
        self.ns_socket.send(command)
        buf = ""
        while True:
            tmp = self.ns_socket.recv(8192)
            buf += tmp.decode("utf-8")
            if b'\nrep 002' in tmp or tmp == '':
                break
        return buf

    def authentificate():
        print()

    def cmd_list_users(self, exp='', return_list=False):
        buf = self.send_command(b'list_users\n')
        users_string = buf.split('\n')[:-2]
        users = []
        user_format = ['Socket', 'Login', 'IP', 'Login timestamp',
                'State timestamp', 'Location', 'Group', 'State', 'User Data']
        for u in users_string:
            lu = u.split(' ')
            user = {}
            i = 0
            for col in user_format:
                data = lu[i]
                if i == 3:
                    user[col] = time.ctime(int(data))
                elif i == 4:
                    user[col] = str(int(time.time()) - int(data))
                elif col == 'State':
                    tmp = data.split(':')
                    if len(tmp) > 1:
                        tmp[1] = time.strftime("%Hh %Mm %Ss",
                                    time.gmtime(int(time.time()) - int(tmp[1])))
                        data = ':'.join(tmp)
                    user[col] = data
                else:
                    user[col] = data
                i += 1
                if i == 5:  # Hack for skipping trust level and ws type rows
                    i = 8
            users.append(copy.deepcopy(user))

        # Matching exp
        if exp != '':
            match_users = []
            for u in users:
                for field  in u.values():
                    if exp in field:
                        match_users.append(u)
                        break
            users = match_users

        # Special return for interactive mode
        if return_list:
            users_list = []
            users_list.append(user_format)
            for u in users:
                user = []
                for col in user_format:
                    user.append(u[col])
                users_list.append(user)
            return users_list
        # Format return for API calls
        # TODO: export to json and call and create direct command line to do it
        return [user_format, users]
