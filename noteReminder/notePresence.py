import subprocess
import os
from subprocess import Popen

def show(noteFile):
    p = Popen(['notepad', noteFile])