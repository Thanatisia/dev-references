"""
gtts (Google Text-to-Speech) testbench/practice ground for use for AI with NLP
"""
import os
import sys

## For GTTS
from subprocess import PIPE, Popen
from gtts import gTTS

## For Audio Output
from io import BytesIO
from pygame import mixer
import time

def init():
    """
    Initialize Objects
    """

def speak(tts):
    # Initialize Mixer object
    mixer.init()

    # Initialize and create music file pointer memory bytes
    mp3_fp = BytesIO()

    # Write the TTS into the filepointer memory
    tts.write_to_fp(mp3_fp)

    # Set the pointer cursor to the first address in the memory
    mp3_fp.seek(0)

    # Load the music you want to play in the file pointer to the mixer
    mixer.music.load(mp3_fp, "mp3")

    # Begin audio output
    mixer.music.play()

def text_to_speech(text):
    # Initialize Variables
    audio_output_file_Name = "audio-out.mp3"

    try:
        # Initialize GTTS speaker class objects by importing the text to output
        # and Try to perform Text-to-Speech conversion and Audio Output
        speaker = gTTS(text=text, lang="en", slow=False)

        # Save the resulting text file audio output as a mp3 audio file
        speaker.save(audio_output_file_Name)

        # Begin speaking
        speak(speaker)

        time.sleep(5)
    except Exception as ex:
        print("Exception: {}".format(ex))

def main():
    # Initialize Variables
    text="Hello World!"

    text_to_speech(text)

if __name__ == "__main__":
    init()
    main()

