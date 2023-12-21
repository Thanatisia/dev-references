"""
SpeechRecognition testbench/practice ground for use for AI with NLP
"""
import os
import sys
import speech_recognition as sr

def init():
    """
    Initialize Objects
    """
    global recognizer, pyaudio

    # Initialize Speech Recognizer object
    recognizer = sr.Recognizer()
    pyaudio = sr.Microphone().get_pyaudio()

def list_Microphones():
    # Initialize Variables
    mic_List = []

    # Begin listening to speech with the Microphone object
    with sr.Microphone() as mic:
        mic_List = mic.list_microphone_names()
    
    return mic_List

def listen_audio():
    # Initialize Variables
    audio = ""

    # Try to open the Microphone class object
    mic = sr.Microphone()

    if mic:
        # Microphone opened
        print("[+] Microphone successfully opened.")

        with mic:
            # Listen to the Microphone's Audio input using the speech recognizer class
            print("Listening...")
            audio = recognizer.listen(mic)

            if audio != None:
                print("[+] Audio detected")
            else:
                print("[-] No Audio detected.")

        # Close microphone after use
        if mic != None:
            if mic.stream != None:
                mic.stream.close()
                print("[+] Microphone closed.")
    else:
        print("No microphone detected.")

    return audio

def speech_to_text(audio, method="google"):
    # Try to perform speech recognition
    try:
        # Try to recognize the Text from the audio using Google's API and return it into a variable
        print("Converting using: {}".format(method))
        match method:
            case "google":
                text = recognizer.recognize_google(audio)
            case _:
                print("Invalid speech format: {}".format(method))
    except Exception as ex:
        text = str(ex)

    return text

def main():
    # Initialize Variables
    mic = None

    audio = listen_audio()
    text = speech_to_text(audio)
    if text != "":
        print("Message: {}".format(text))
    else:
        print("No message given.")

if __name__ == "__main__":
    init()
    main()

