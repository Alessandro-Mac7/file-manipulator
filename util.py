import os
import re

dir_path = r"C:\Users\sciam\Downloads\cibus"
files = os.listdir(dir_path)

profiles = []

for file in files:

    with open(os.path.join(dir_path,file),'r') as f:
        for line in f.readlines():

            if line.find("fooddb_flavor_profile") != -1:
                line = line.strip()  # or some other preprocessing
                line = line.replace("fooddb_flavor_profile", "")
                line = line.replace("\"", "")
                line = line.replace(":", " ")
                line = line.replace(",", " ")
                line = line.replace("@", " ")
                profiles.append(line)  # storing everything in memory!

distinct_flavor = set(profiles)

print(distinct_flavor)


