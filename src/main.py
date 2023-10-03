import os
import sys
import json

def read_file(name):
    with open(name) as file:
        # returns dict
        contents = file.read()
        parsed = json.loads(contents)
        return parsed

def write_file(name, d):
    with open(name, "w") as file:
        json.dump(d, file)

def place(name, data):
    dir = os.getcwd()
    data[sys.argv[2]] = dir
    write_file(name, data)

def remove(name, data):
    del data[sys.argv[2]]
    write_file(name, data)

def main():
    commands = {"place" : place, "del" : remove}
    filename = "/Users/aleksimpson/Desktop/projects/waypoint/src/store.json"

    # load json
    paths = read_file(filename)
    # get args
    if sys.argv[1] in commands.keys(): 
        commands[sys.argv[1]](filename, paths)
    else: 
        if not sys.argv[1] in paths.keys():
            print("invalid command")
        else:
            os.chdir(paths[sys.argv[1]])

main()
os.system("fish")
