import requests
import colorama
from colorama import Fore, Style, init
import os
import subprocess
import time
import webbrowser

init(convert=True)

print(f"""
{Fore.CYAN}¸„.-•~¹°”ˆ˜¨ WELCOME ¨˜ˆ”°¹~•-.„¸{Style.RESET_ALL}
    {Fore.MAGENTA}To Auto Coder Installer!{Style.RESET_ALL}
    ------------------------
""")
time.sleep(1.5)
def nicefy_app_name(appname):
    print(f"""
    Now Downloading & Installing {Fore.BLUE}>>{Style.RESET_ALL} '{Fore.GREEN}{appname}{Style.RESET_ALL}' {Fore.BLUE}<<{Style.RESET_ALL}
    
    {Fore.YELLOW}Please be patient :){Style.RESET_ALL}\n\n
    """)

#Visual Studio Code
nicefy_app_name("VSC")
vsc_url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
vsc = requests.get(vsc_url, allow_redirects=True)
open('vscinstaller.exe', 'wb').write(vsc.content)
#Silent install Switches = /VERYSILENT /NORESTART /MERGETASKS=!runcode
#Silent install cmd `start vscinstaller.exe /VERYSILENT /NORESTART /MERGETASKS=!runcode`
os.system('start vscinstaller.exe /VERYSILENT /NORESTART /MERGETASKS=!runcode')

#Atom
nicefy_app_name("Atom")
atom_url = 'https://atom.io/download/windows_x64'
atom = requests.get(atom_url, allow_redirects=True)
open('atominstaller.exe', 'wb').write(atom.content)
#Silent install switches = /s
#Silent install cmd `start atominstaller.exe /s`
os.system('start atominstaller.exe /s')

#Python
nicefy_app_name("Python")
python_url = 'https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe'
python = requests.get(python_url, allow_redirects=True)
open('pythoninstaller.exe', 'wb').write(python.content)
#Silent install swithces = /quiet /PrependPath
#Silent install cmd `start pythoninstaller.exe /quiet /PrependPath`
os.system('start pythoninstaller.exe /quiet /PrependPath')

#NodeJS
nicefy_app_name("NodeJS")
nodejs_url = 'https://nodejs.org/dist/v14.15.4/node-v14.15.4-x64.msi'
nodejs = requests.get(nodejs_url, allow_redirects=True)
open('nodejsinstaller.msi', 'wb').write(nodejs.content)
#Silent install cmd = msiexec.exe /i nodejsinstaller.msi /quiet
os.system('msiexec.exe /i nodejsinstaller.msi /quiet')


webbrowser.open('https://elite-dev.tk/thankyou')