### Download channels from the database :)

git --version

FILE_PATH="orgchannels/README.md"

if [ -f "$FILE_PATH" ]; then
    git pull https://github.com/MakiDevelops/orgchannels
else
    git clone https://github.com/MakiDevelops/orgchannels
fi



