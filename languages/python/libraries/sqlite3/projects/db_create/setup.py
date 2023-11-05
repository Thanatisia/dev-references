"""
General setup and pre-initialization steps
"""
import os
import sys
import env
from env import Env

class Setup():
    def __init__(self):
        self.start()

    def start(self):
        """
        Begin Pre-Initialization Setups
        """
        # Initialize Variables
        self.cs_Env = Env()
        self.env = self.cs_Env.env_var

        # Source Environment Variables
        self.cs_Env.source()


