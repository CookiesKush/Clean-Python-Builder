import os
import shutil
import base64
import random
from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore
from util.plugins.common import *

temp = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp'

def builder(fileName, scriptName, obfuse):
    setTitle(f"Compiling {fileName}.py => {scriptName}.exe") 
    print(f"\n{Fore.RESET}Compiling {Fore.GREEN}{fileName}.py {Fore.RESET}into {Fore.RED}{scriptName}.exe{Fore.YELLOW}\n")
    try:
        if obfuse == True:
            IV = Random.new().read(AES.block_size)
            key = u''
            for i in range(8):
                key = key + chr(random.randint(0x4E00, 0x9FA5))

            with open(temp + f'\\{fileName}.py') as f: 
                _file = f.read()
                imports = ''
                input_file = _file.splitlines()
                for i in input_file:
                    if i.startswith("import") or i.startswith("from"):
                        imports += i+';'

            with open(temp + f'\\{fileName}.py', "wb") as f:
                encodedBytes = base64.b64encode(_file.encode())
                obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
                f.write(f'from Crypto.Cipher import AES;{imports}exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())
            
            shutil.move(temp + f'\\{fileName}.py', f"{os.getcwd()}\\{fileName}.py")


        os.system(f"pyinstaller --onefile --clean --log-level=INFO -n {fileName} {fileName}.py")


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

        