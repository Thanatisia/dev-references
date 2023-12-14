import os
import sys
from subprocess import Popen, PIPE

def get_block_Information(disk_Label):
    """
    Obtain block information regarding the disk using 'blkid' and
    return the information formatted as a dictionary

    :: Params
    - disk_Label : Your target disk label; i.e. SATA|AHCI = /dev/sdX, NVME = /dev/nvme[disk-number], Loopback = /dev/loop[disk-number]
    """
    # Initialize Variables
    block_Information = {disk_Label : []}
    cmd_str = "blkid".format(disk_Label)
    stdout = None
    stderr = None
    resultcode = -1

    # Open subprocess pipe for communication to Obtain block information
    with Popen(cmd_str.split(), stdin=PIPE, stdout=PIPE) as open_Subprocess:
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

    # Format stdout to block information
    if stdout != None:
        # Split standard output into rows of entries
        block_Entries = stdout.split("\n")[::-1][1:][::-1]

        # Iterate through every row
        for i in range(len(block_Entries)):
            # Get current row
            curr_row = block_Entries[i]

            # Split the current row by the spacing
            curr_row_spl = curr_row.split(" ")

            # Split the first element by the delimiter ': '
            partition_label = curr_row_spl[0].split(":")[0]

            # Check if specified partition label is in the disk label string
            if (len(partition_label.split(disk_Label)) > 1):
                # After split, there are multiple entries because split was successful

                # Get partition number from partition label
                partition_Number = partition_label.split(disk_Label)[1:][0]

                # Obtain other block info
                curr_row_block_Info = curr_row_spl[1:]

                # Split the block info into keywords and values
                curr_row_block_Mapping = {
                    "partition-label" : partition_label,
                    "device-uuid" : curr_row_block_Info[0].split("=")[1],
                    "block-size" : curr_row_block_Info[1].split("=")[1],
                    "filesystem-type" : curr_row_block_Info[2].split("=")[1],
                    "partuuid" : curr_row_block_Info[3].split("=")[1]
                }

                # Map current row disk label to the block information
                block_Information[disk_Label].append(
                    {
                        partition_Number : curr_row_block_Mapping
                    }
                )

    return block_Information

def main():
    disk_Label = "/dev/sda"
    block_Info = get_block_Information(disk_Label)
    print("Block Information: {}".format(block_Info))

if __name__ == "__main__":
    main()
