import requests
import colorama
from colorama import Fore, Style
import python as pythoninstaller

print(f"""
{Fore.CYAN}¸„.-•~¹°”ˆ˜¨ WELCOME ¨˜ˆ”°¹~•-.„¸{Style.RESET_ALL}
    {Fore.MAGENTA}To Auto Coder Installer!{Style.RESET_ALL}
""")

def nicefy_app_name(appname):
    print(f"""
    Now Downloading {Fore.BLUE}>>{Style.RESET_ALL} '{Fore.GREEN}{appname}{Style.RESET_ALL}' {Fore.BLUE}<<{Style.RESET_ALL}
    
    {Fore.YELLOW}Please be patient :){Style.RESET_ALL}
    """)

#Visual Studio Code
nicefy_app_name("VSC")
vsc_url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
vsc = requests.get(vsc_url, allow_redirects=True)
open('vscinstaller.exe', 'wb').write(vsc.content)


#Atom
nicefy_app_name("Atom")
atom_url = 'https://atom.io/download/windows_x64'
atom = requests.get(atom_url, allow_redirects=True)
open('atominstaller.exe', 'wb').write(atom.content)

#Python
nicefy_app_name("Python")
python_url = 'https://www.python.org/ftp/python/3.9.1/python-3.9.1-amd64.exe'
python = requests.get(python_url, allow_redirects=True)
open('pythoninstaller.exe', 'wb').write(python.content)