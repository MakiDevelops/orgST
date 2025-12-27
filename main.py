# Some notes:
# 1. Imports go at top of file for readability
# 2. Please dont import entire modules, just what you need
# 3. Dont use `subprocess` since generally its not cross-platform due to differences in commands on systems
# 4. When you use subprocesses, use `subprocess.run` not `os.system` as the first is safer,
#       also do NOT allow user input in commands at all
#       (say `system(f"echo {some_user_input}")` and the user types in "; sudo dd if=/dev/zero of=/dev/sda bs=1M")
# 5. Always check return codes when available (for commands, 0=success, >0=error)
# 6. When making command things, use an LUT (lookup table)
from os import getcwd

from git import Repo as gitrepo  # pip install GitPython

terminal_name = "orgST Terminal"
version = 1.0
date_edited = "2025-12-24"

dir = getcwd()
border = "+---------------------------+"
ticon = "[>] "
cmd_list = ["help", "run", "ID", "info", "git", "time", "test"]


def cls():
    print("\033[H\033[2J")


def orgfetch():
    cls()
    print("                 _____ _____  ")
    print("                /  ___|_   _| ")
    print("  ___  _ __ __ _\\ `--.  | |   ")
    print(" / _ \\| '__/ _` |`--. \\ | |   ")
    print("| (_) | | | (_| /\\__/ / | |   ")
    print(" \\___/|_|  \\__, \\____/  \\_/   ")
    print("            __/ |             ")
    print("           |___/              ")
    print(border)
    print(f"{terminal_name} {version}.")
    print(f"Last edited: {date_edited}")


def dotest():
    fpath = "./orgchannels"
    try:
        gitrepo(fpath).remotes.origin.pull()  # If this fails, assume its NOT a git repo
        #       (we could check for ENOENT on fpath/.git, but its possible its a bad .git dir)
    except:
        gitrepo.clone_from(
            "https://github.com/MakiDevelops/orgchannels", "./orgchannels"
        )


cmds = {
    "help": lambda: print("help, run, ID, info, git, time, test"),
    "info": orgfetch,
    "test": dotest,
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
            print("Command not found.")


if __name__ == "__main__":
    main()
