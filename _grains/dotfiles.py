import os, pwd
from os import path

def main():
    return {
        'home': pwd.getpwuid(os.getuid()).pw_dir,
    }
