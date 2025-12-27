#### Imports:
import os
import sys
import time
from time import sleep

### Information:
terminal_name = "orgST Terminal"
main_authors = "makidevelops, wdboyes13"
contributors = "chureki (TableDev)"
version = 1.0
date_edited = "2025-12-27"

## Vars:
dir = os.getcwd()
border = "+---------------------------+"
ticon = "[>] "
cmd_list = ["help", "run", "ID", "info", "git", "time", "test", "exit"]
runlist = ["C", "exit"]


def cls():
    print("\033[H\033[2J")


def orgfetch():
    cls()
    print("                 _____ _____  ")  # the sleep stuff is to make it look cool!
    sleep(0.1)
    print("                /  ___|_   _| ")
    sleep(0.1)
    print("  ___  _ __ __ _\ `--.  | |   ")
    sleep(0.1)
    print(" / _ \| '__/ _` |`--. \ | |   ")
    sleep(0.1)
    print("| (_) | | | (_| /\__/ / | |   ")
    sleep(0.1)
    print(" \___/|_|  \__, \____/  \_/   ")
    sleep(0.1)
    print("            __/ |             ")
    sleep(0.1)
    print("           |___/              ")
    sleep(0.1)
    print(border)
    print("a cool open source terminal made by some people")
    print(f"Main authors: {main_authors}")
    print(f"Contributors: {contributors}")
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
                print("help, run, ID, info, git, time, test, exit")
            if inp == "info":
                orgfetch()
            if inp == "exit":
                quit()
            if inp == "run":
                while True:
                    inp = input("C for channelviewer: ")
                    if inp in runlist:
                        if inp == "C":
                            print("it opens it now woah!")
                        if inp == "exit":
                            break
                    else:
                        print("That cannot be run. Type 'exit' to leave the run menu.")

        else:
            print("Command not found.")


if __name__ == "__main__":
    main()
