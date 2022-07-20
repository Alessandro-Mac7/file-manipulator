import os
import json  

dir_path = r"C:\Users\sciam\Downloads\cibus"
files = os.listdir(dir_path)
for file in files:
    print(dir_path + file)
    f=open(os.path.join(dir_path,file),'r')
    
    data = json.load(f)
    w = open(file, "w")
    w.write(json.dumps(data, indent = 1))
    w.close()
    
    f.close()