#!/usr/bin/env python3

# import additional code to complete our task
import shutil
import os

# move into the working dir
os.chdir("/home/student/mycode/")

#copy fileA to fileB
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire dirA to dirB
shutil.copytree("5g_research/", "5g_research_backup/")

