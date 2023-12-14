import os
import sys
from subprocess import Popen, PIPE

def get_subprocess_Communicate(cmd):
    """
    Open a system subprocess and execute a command, then pipe the output and result code into the application interface

    :: Params
    - cmd : The command string or list you wish to execute
    """
    # Initialize Variables
    target_cmd = None
    stdout = None
    stderr = None
    resultcode = -1

    if type(cmd) == str:
        # If is string, split
        cmd = cmd.split()

    # Open subprocess pipe for communication to Obtain block information
    with Popen(cmd, stdin=PIPE, stdout=PIPE) as open_Subprocess:
        # Execute process in sync - check if the previous command is completed before proceeding
        stdout, stderr = open_Subprocess.communicate()

        # Decode and clean-up output
        if stdout != None:
            stdout = stdout.decode("utf-8")

        if stderr != None:
            stderr = stderr.decode("utf-8")
        else:
            stderr = ""

        # Get result code from process pipe
        resultcode = open_Subprocess.returncode

    return stdout, stderr, resultcode

def main():
    # Initialize Variables
    cmd_str = "ping -c 5 8.8.8.8"
    cmd_list = ["ping", "-c", "5", "8.8.8.8"]

    # Execute command string test
    stdout, stderr, resultcode = get_subprocess_Communicate(cmd_str)
    print("Command String:")
    print("Result Code: {}".format(resultcode))
    print("Standard Output: {}".format(stdout))
    print("Standard Error: {}".format(stderr))

    # Execute command list test
    stdout, stderr, resultcode = get_subprocess_Communicate(cmd_list)
    print("Command List:")
    print("Result Code: {}".format(resultcode))
    print("Standard Output: {}".format(stdout))
    print("Standard Error: {}".format(stderr))

if __name__ == "__main__":
    main()
