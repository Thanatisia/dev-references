"""
Environment Variable handling
"""
import os
import sys

class Env():
    """
    Environment Variable class
    """
    def __init__(self):
        # Initialize Variables
        self.env_var:dict = {
            # [key] : [value]
            # key = The environment variable keyword
            # value = the value
            "DATABASE_PATH" : "",
            "DATABASE_NAME" : ""
        }

    def list_all_Env(self):
        """
        List all environment variable keys and values
        """
        for k,v in self.env_var.items():
            print("{} = {}".format(k,v))

    def get_Value(self, keyword):
        """
        Get value of keyword in environment variable dictionary
        """
        return self.env_var[keyword]

    def source(self):
        """
        Source Environment Variables
        """
        # Initialize Variables
        env_var = self.env_var

        # Loop through all keywords and source
        for k,_ in env_var.items():
            # Get environment variable of keyword
            v = os.environ.get(k)

            # Map environment variable keyword to value
            env_var[k] = v

        # Replace global variable
        self.env_var = env_var

    def source_from_File(self, cfg_file="config.txt"):
        """
        Source environment variable from file
        """
        # Initialize Variables
        env_var = self.env_var

        # Open Configuration File for reading
        with open(cfg_file, "r") as read_config:
            # Read file contents

            ## Read first line
            line = read_config.readline()

            while line != "":
                # Still have line

                # Split the line into delimiters
                spl_v = line.split()

                # Get indexes
                keyword = spl_v[0]
                delimiter = spl_v[1]
                value = spl_v[2]

                # Map environment variable keyword to value
                env_var[keyword] = value

                # Read next line
                line = read_config.readline()

            # Close file after usage
            read_config.close()

        # Replace global variable
        self.env_var = env_var


