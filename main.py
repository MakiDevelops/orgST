#### Information:
terminal_name = 'orgST Terminal'
version = 1.0
date_edited = '2025-12-24'

### Imports:
import os, time, sys

## Vars:
dir = os.getcwd()
border = '+---------------------------+'
ticon = '[>] ' 
cmd_list = ['help', 'run', 'ID', 'info', 'git', 'time','test']

def orgfetch():
    print("                 _____ _____  ")
    print("                /  ___|_   _| ")
    print("  ___  _ __ __ _\ `--.  | |   ")
    print(" / _ \| '__/ _` |`--. \ | |   ")
    print("| (_) | | | (_| /\__/ / | |   ")
    print(" \___/|_|  \__, \____/  \_/   ")
    print("            __/ |             ")
    print("           |___/              ")
    print(border)
    print(f"{terminal_name} {version}.")
    print(f"Last edited: {date_edited}")
    

def main():
    print(f"{terminal_name} {version}.")
    print(f"Last edited: {date_edited}")
    print(dir)
    print(border)

    while True:
        inp = input(ticon)
        if inp in cmd_list:
            if inp == "help":
                print("help, run, ID, info, git, time, test")
            if inp == 'info':
                orgfetch()
            if inp == 'test':
                os.system('chmod +x getchannels.sh')
                os.system('./getchannels.sh')
        else:
            print("Command not found.")


if __name__ == "__main__":
    main()
