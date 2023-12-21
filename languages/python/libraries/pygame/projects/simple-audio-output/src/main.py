"""
gtts (Google Text-to-Speech) testbench/practice ground for use for AI with NLP
"""
import os
import sys
import time
from subprocess import PIPE, Popen
from pygame import mixer
from io import BytesIO

def init():
    """
    Initialize Objects
    """

def text_to_speech(text):
    # Initialize Variables
    audio_output_file_Name = "audio-out.mp3"

    try:
        # Initialize and create MP3 File pointer bytes
        mp3_fp = BytesIO()

        mixer.init()

    except Exception as ex:
        print("Exception: {}".format(ex))

def main():
    # Initialize Variables
    text="Hello World!"

    text_to_speech(text)

if __name__ == "__main__":
    init()
    main()

