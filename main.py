# Some notes:
# 1. Imports go at top of file for readability
# 2. Please dont import entire modules, just what you need
# 3. Dont use `subprocess` since generally its not cross-platform due to differences in commands on systems
# 4. When you use subprocesses, use `subprocess.run` not `os.system` as the first is safer,
#       also do NOT allow user input in commands at all
#       (say `system(f"echo {some_user_input}")` and the user types in "; sudo dd if=/dev/zero of=/dev/sda bs=1M")
# 5. Always check return codes when available (for commands, 0=success, >0=error)
# 6. When making command things, use an LUT (lookup table)
#
from os import getcwd
from time import sleep

from git import Repo as gitrepo  # pip install GitPython

terminal_name = "orgST Terminal"
main_authors = "makidevelops, wdboyes13"
contributors = "chureki (TableDev)"
version = 1.0
date_edited = "2025-12-27"
spdxid = "MIT"

dir = getcwd()
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
    print(border)
    print("Copyright (c) 2025 Wdboyes13, MakiDevelops. All rights reserved.")
    print(f"SPDX-License-Identifier:{spdxid}")


def dotest():
    fpath = "./orgchannels"
    try:
        gitrepo(fpath).remotes.origin.pull()  # If this fails, assume its NOT a git repo
        #       (we could check for ENOENT on fpath/.git, but its possible its a bad .git dir)
    except:
        gitrepo.clone_from(
            "https://github.com/MakiDevelops/orgchannels", "./orgchannels"
        )


def dorun():
    while True:
        inp = input("C for channelviewer, 'exit' to leave. [>] ")
        if inp in runlist:
            if inp == "C":
                print("it opens it now woah!")
            if inp == "exit":
                break
        else:
            print("That cannot be run. Type 'exit' to leave the run menu.")


cmds = {
    "help": lambda: print("help, run, ID, info, git, time, test"),
    "info": orgfetch,
    "test": dotest,
    "exit": quit,
    "run": dorun,
    "git": lambda: print(
        "Go check out the repo @ https://github.com/MakiDevelops/orgST"
    ),
}


def main():
    print(f"{terminal_name} {version}.")
    print(f"Last edited: {date_edited}")
    print(dir)
    print(border)

    while True:
        inp = input(ticon)
        if inp in cmds:
            cmds[inp]()
        else:
            print("Command not found. Type 'help' for command lists.")


if __name__ == "__main__":
    main()
