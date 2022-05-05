import os
import shutil
from colorama import Fore
from util.plugins.common import *

def builder(fileName, scriptName):
    setTitle(f"Compiling {fileName}.py => {scriptName}.exe") 
    print(f"\n{Fore.RESET}Compiling {Fore.GREEN}{fileName}.py {Fore.RESET}into {Fore.RED}{scriptName}.exe{Fore.YELLOW}\n")
    try:
        os.system(f"pyinstaller --clean --onefile -n {scriptName} {fileName}.py") 
        shutil.move(f"{os.getcwd()}\\dist\\{scriptName}.exe", f"{os.getcwd()}\\{scriptName}.exe") 
        shutil.rmtree('build')
        shutil.rmtree('dist')
        os.remove(f'{scriptName}.spec') 

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Error while making exe: {Fore.RESET}{e}")
        try:
            shutil.rmtree('build')
            shutil.rmtree('dist')
            os.remove(f'{scriptName}.spec')
        except FileNotFoundError:
            pass
    else:
        setTitle("Finished Creating exe!")
        print(f"\n{Fore.GREEN}Finished Creating exe\n")
    input(f'{Fore.RESET}[{Fore.GREEN}>>>]{Fore.RESET} Enter anything to continue . . .')