#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os


#file_name = input("Enter the name of the file")
#dir_name = input("Enter the name of the dir")

#def copy_file():
    #enter the dir    
#    os.chdir("/home/student/mycode/testing")

    # copy the fileA to fileB
#    if shutil.copy(f"{file_name}.txt", f"{file_name}.txt.copy"):
#        return True
#    else:
#        return False
    

def copy_dir():
    # enter the dir
    os.chdir("/home/student/mycode/testing")
    # copy the entire directoryA to directoryB
    if shutil.copytree(f"6g/", f"6g_backup/"):
        return True
    else:
        return False


#def test_copy_file(monkeypatch):
#    assert copy_file() == os.path.isfile(f'/home/student/mycode/testing/{file_name}.txt.copy')
    
#    monkeypatch.setattr(target, name, value,raising= True)

def test_copy_dir():
    assert copy_dir() == os.path.isdir(f'/home/student/mycode/testing/6g_backup/')

