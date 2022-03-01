import os, shutil, ctypes, platform
from colorama import Fore

def setTitle(str):
    system = platform.system()
    if system == 'Windows':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{str}")
    else:
        os.system(f"\033]0;{str}\a")

def builder(fileName, scriptName):
    setTitle(f"Compiling {fileName}.py -> {scriptName}.exe | github.com/Callumgm ") 
    print(f"\n{Fore.RESET}Compiling {Fore.GREEN}{fileName}.py {Fore.RESET}into {Fore.RED}{scriptName}.exe{Fore.YELLOW}\n")
    try:
        os.system(f"pyinstaller --onefile  -n {scriptName} {fileName}.py") # Command to compile script
        shutil.move(f"{os.getcwd()}\\dist\\{scriptName}.exe", f"{os.getcwd()}\\{scriptName}.exe") # Moves built file from dist folder to current folder
        shutil.rmtree('build') # Removes uneeded directories / files after compiling
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{scriptName}.spec') 

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}Error while making exe: {Fore.RESET}{e}")
        # Remove files if any errors (to keep it clean)
        try:
            shutil.rmtree('build')
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
            os.remove(f'{scriptName}.spec')
        except FileNotFoundError:
            pass
    else:
        setTitle("Finished Creating exe! | github.com/Callumgm ")
        print(f"\n{Fore.GREEN}Finished Creating exe\n")
    input(f'{Fore.RESET}[{Fore.GREEN}>>>]{Fore.RESET} Enter anything to continue . . .')