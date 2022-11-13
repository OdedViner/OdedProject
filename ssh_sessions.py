from hepler import input_string

import paramiko
import threading


class ConnectSSH(object):
    def __init__(self):
        self.count = 0
        self.dict_output = dict()

    def run_cmd_via_ssh(self, destination_ip, username, password, cmd):
        # Create object of SSHClient and
        ssh = paramiko.SSHClient()
        # AutoAddPolicy for missing host key to be set before connection setup.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            destination_ip, port=22, username=username, password=password, timeout=3
        )
        # using exec_command
        stdin, stdout, stderr = ssh.exec_command(cmd)
        self.dict_output[f"{destination_ip}_{self.count}"] = stdout.read()
        self.count += 1

    def run_multiple_ssh_sessions(
        self, params
    ):
        thread_list = list()
        for param in params:
            thr = threading.Thread(
                target=self.run_cmd_via_ssh,
                args=(param["destination_ip"], param["username"], param["password"], param["cmd"])
            )
            thread_list.append(thr)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

        print(self.dict_output)


def main():
    number_of_sessions = input_string(string_text="number_of_session", default_value="2")
    list_param = list()
    for i in range(int(number_of_sessions)):
        destination_ip_address = input_string(string_text="ip address", default_value="127.0.0.1")
        username = input_string(string_text="username", default_value="odedviner")
        password = input_string(string_text="password")
        cmd = input_string(string_text="command", default_value="pwd")
        list_param.append( {
            "destination_ip": destination_ip_address,
             "username": username,
             "password": password,
             "cmd": cmd
        })
    ssh_instance = ConnectSSH()
    ssh_instance.run_multiple_ssh_sessions(list_param)


if __name__ == '__main__':
    main()
