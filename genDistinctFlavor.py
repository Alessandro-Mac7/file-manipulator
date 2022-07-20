profiles = []
with open(r"D:\Project\flavorDB\Search2.txt") as file:
    for line in file:
        line = line.strip()  # or some other preprocessing
        profiles.append(line)  # storing everything in memory!
distinct_flavor = set(profiles)

print(distinct_flavor)
