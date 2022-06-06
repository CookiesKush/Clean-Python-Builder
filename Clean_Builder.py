import os, sys
from time import sleep
from colorama import Fore
from util.build import *
from util.plugins.common import *


def main():
    setTitle("Cookies Clean Builder")
    clear()
    print(f"{Fore.LIGHTRED_EX}Please place file u wish to compile in the same directory as this script")
    sleep(2)
    clear()
    print(f"""
    
            {Fore.CYAN}Welcome to Cookies clean builder {Fore.RESET} :)

        {Fore.GREEN}https://github.com/Callumgm

    {Fore.RESET}[{Fore.GREEN}1{Fore.RESET}] {Fore.CYAN}Clean Compile File
    {Fore.RESET}[{Fore.GREEN}420{Fore.RESET}] {Fore.LIGHTRED_EX}Exit Builder
    
    """)

    choice = str(input(f"{Fore.LIGHTMAGENTA_EX}Choose a number {Fore.YELLOW}>> "))

    if choice == "1":
        fileName = str(input(f"{Fore.CYAN}Enter the name of the file u wish to compile {Fore.YELLOW}>> "))
        scriptName = str(input(f"{Fore.CYAN}Enter output name for comiled exe file {Fore.YELLOW}>> "))
        obfuse = bool(input(f"{Fore.CYAN}Do u want to obfuscate source code for extra security? {Fore.RESET}({Fore.CYAN}Leave empty for no{Fore.RESET}) {Fore.YELLOW}>> "))
        clear()
        builder(fileName, scriptName, obfuse)

    elif choice == "420":
        clear()
        print(f"{Fore.CYAN}You will be missed :) {Fore.RESET}")
        sleep(2)
        sys.exit(0)
    
    else:
        print(f"{Fore.LIGHTRED_EX}Please choose a number!{Fore.RESET}")
        sleep(2)
        main()


main()








