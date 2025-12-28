from time import sleep

from git import Repo as gitrepo
from git import exc as gexcepts

from texts.info import logo
from texts.prompts import ftprompt, mprompt, ticon

cmd_list = ["help", "run", "ID", "info", "git", "time", "test", "exit"]
runlist = ["C", "exit"]


def cls():
    print("\033[H\033[2J")


def orgfetch():
    cls()
    for line in logo:
        print(line)
        sleep(0.1)  # 100ms sleep, looks cooler
    print(ftprompt)


def dotest():
    fpath = "./orgchannels"
    try:
        gitrepo(fpath).remotes.origin.pull()
    except gexcepts.InvalidGitRepositoryError or gexcepts.NoSuchPathError:
        gitrepo.clone_from("https://github.com/MakiDevelops/orgchannels", fpath)


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
    print(mprompt)
    while True:
        inp = input(ticon)
        if inp in cmds:
            cmds[inp]()
        else:
            print("Command not found. Type 'help' for command lists.")


if __name__ == "__main__":
    main()
