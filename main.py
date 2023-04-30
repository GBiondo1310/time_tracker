import argparse
import json
import os
from datetime import datetime, timedelta
from math import floor

FORMAT = "%Y/%m/%d %H:%M:%S"

parser = argparse.ArgumentParser(description="Track code time",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument("-a", "--archive", action="store_true", help="archive mode")
# parser.add_argument("-v", "--verbose", action="store_true", help="increase verbosity")
# parser.add_argument("-B", "--block-size", help="checksum blocksize")
# parser.add_argument("--ignore-existing", action="store_true", help="skip files that exist")
# parser.add_argument("--exclude", help="files to exclude")
# parser.add_argument("src", help="Source location")
# parser.add_argument("dest", help="Destination location")
# args = parser.parse_args()
# config = vars(args)
# print(config)

parser.add_argument("-s", "--start", action = "store_true", help="Start time tracker.", )
parser.add_argument("-e", "--end", action ="store_true", help="End time tracker.")
parser.add_argument("-g", "--get", action ="store_true", help="Get working time for this project.")
args = parser.parse_args()
config = vars(args)

def check_timetrack_existence():
    return ".timetrack" in os.listdir()

def curdir():
    return list(reversed(os.getcwd().split('/')))[0]

def start_tracker():
    if check_timetrack_existence():
        with open(".timetrack", mode="r") as jsonfile:
            data:dict = json.load(jsonfile)
    else:
        print(".timetrack file not present, creating one...")
        data = {}

    for value in data.values():
        if not value:
            print("There's an open time track, please stop it with 'timetrack -e' or edit the .timetrack file before starting a new tracking session.")
            return
    now = datetime.now()
    data.update({now.strftime(FORMAT):False})

    with open(".timetrack", mode="w") as jsonfile:
        json.dump(data, jsonfile, indent = 4)

    print(f"Started time tracking on project: {curdir()} at {now.strftime(FORMAT)}.\nRemember to launch 'timetrack -e' to stop tracking time on {curdir()}.")

def end_tracker():
    if check_timetrack_existence():
        with open(".timetrack", mode="r") as jsonfile:
            data:dict = json.load(jsonfile)

        for key, value in data.items():
            print(data)
            if not value:
                now = datetime.now()
                data.update({key:[now.strftime(FORMAT), (now-datetime.strptime(key, FORMAT)).total_seconds()]})
                with open(".timetrack", mode="w") as jsonfile:
                    json.dump(data, jsonfile, indent = 4)
                print(f"Ended time tracking on project: {curdir()} at {now.strftime(FORMAT)}.\nYou can get the total amount of time spent on {curdir} with 'timetrack -g'.")
            else:
                print("Not timetrack currently running. Did you forget to start one?")

    else:
        print(".timetrack file does not exist, you need to create one (timetrack -s)")

def get_time():
    if check_timetrack_existence():
        with open(".timetrack", mode="r") as jsonfile:
            data:dict = json.load(jsonfile)
        total_seconds = 0
        for value in data.values():
            if value:
                total_seconds+=value[1]
        total_seconds = floor(total_seconds)
        print(total_seconds)
        minutes = floor(total_seconds/60) if total_seconds/60 >= 1 else 0
        print(minutes)
        hours = floor(minutes/60) if minutes/60>=0 else 0
        print(hours)
        seconds = int(round(((total_seconds/60)-minutes)*60))
        minutes = int(round((minutes/60-hours)*60))
        hours = int(hours)
        print(f"You're working on {curdir()} project for:\n{hours} hours\n{minutes} minutes\n{seconds} seconds.")
        for key, value in data.items():
            if not value:
                print(f"You have an open timetracker session on {curdir()} project, started at {key}.")
            
    else:
        print(".timetrack file does not exist, you need to create one (timetrack -s)")


if config.get("start"):
    start_tracker()
elif config.get("end"):
    end_tracker()
elif config.get("get"):
    get_time()

