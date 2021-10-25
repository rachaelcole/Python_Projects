# An SSH client using Paramiko
# Paramiko uses PyCrypto and gives simple access to the SSH2 protocol
# http://www.paramiko.org/
# https://github.com/paramiko/paramiko

import paramiko


def ssh_command(ip, port, user, passwd, command):
    """Makes a connection to an SSH server and runs a single command."""
    client = paramiko.SSHClient()
    # Set the policy to accept the SSH key for the SSH server we are connecting to:
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    _, stdout, stderr = client.exec_command(command)  # Run the command we passed in the function call
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())


if __name__ == '__main__':
    import getpass  # Module to get the username from current environment
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()  # Requests the password without displaying user input to console

    ip = input('Enter server IP: ') or '192.168.1.203'
    port = input('Enter port or <CR>: ') or 2222
    command = input('Enter command or <CR>: ') or 'id'

    ssh_command(ip, port, user, password, command)  # Send inputted variables to be executed
