"""This is the main file run this to run the VoiceBot"""
import subprocess
import webbrowser
from colorama import Fore, Style
from speach_to_text import get_text

while True:
    # This listens for voice and returns a strin if found, 0 if not found anytthing
    TEXT = get_text()

    # Check if we got any TEXT, if only silent it is int
    if isinstance(TEXT, int):
        pass

    # For Open Programs Part
    elif TEXT[:4] == 'open':  # Check if first 4 character == open
        TEXT = TEXT.replace('open', '').strip()  # Cleaning TEXT

        try:
            print(f"Opening {TEXT}")
            subprocess.call(TEXT)

        except FileNotFoundError:
            print(f'{Fore.RED}It seems that the path to the program ', end='')
            print(f'"{TEXT}" is not set in Environment variables')
            print(f'Plz add it to the PATH to be able to use it {Style.RESET_ALL}')

    # For Search the web Part
    elif TEXT[:6] == 'search':  # Check if first 6 character == search
        # Cleaning TEXT
        if TEXT[:10] == 'search for':  # Check if first 10 character == search for
            TEXT = TEXT.replace('search for', '', 1)
        else:
            TEXT = TEXT.replace('search', '', 1)
        TEXT = TEXT.strip()

        print(f"Searching for {TEXT}")

        # Opening browser and search for TEXT
        webbrowser.open(f"https://duckduckgo.com/?q={TEXT}")

    # For echo Part
    elif TEXT[:4] == 'type':
        TEXT = TEXT.replace('type', '', 1).strip()
        print(TEXT)

    # For not set a command
    else:
        print(f'{Fore.RED}Cant find command "{TEXT}"{Style.RESET_ALL}')
