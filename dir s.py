from os.path import exists
import os

def drives(drive_list = []):
    for drive in range(ord('A'), ord('Z')):
        if exists(chr(drive) + ':'):
            drive_list.append(chr(drive))
    return drive_list

for disk in drives():
    for top, dirs, files in os.walk(str(disk+":/")):
        for nm in files:
            access = os.path.join(top, nm)
            print(access) #process
