## This is a test file for testing system is able to compile python or not.
import os
import subprocess

print("Hello world!")

cmd = './hello'
retcode = subprocess.call(cmd, shell=True)
