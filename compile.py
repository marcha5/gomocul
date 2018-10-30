#!/usr/local/bin/python3

import subprocess, os

subprocess.run(["rm", "pbrain-STRASBOURG-Marchal.Jonathan.exe", "pbrain-gomocul.spec"], capture_output=True)
subprocess.run(["rm", "-rf", "dist/", "build/", "__pycache__/"], capture_output=True)
#subprocess.run(["pyinstaller", "pbrain-gomocul.py", "comunication_protocol.py", "--onefile", "--name", "pbrain-gomocul.exe"], capture_output=False)
os.system('pyinstaller pbrain-gomocul.py --distpath . -F -n pbrain-STRASBOURG-Marchal.Jonathan.exe')
#subprocess.run(["pyinstaller", "pbrain-gomocul.spec"], capture_output=True)
#subprocess.run(["ln", "-s", "./dist/pbrain-gomocul.exe", "pbrain-STRASBOURG-Marchal.Jonathan.exe"], capture_output=False)
