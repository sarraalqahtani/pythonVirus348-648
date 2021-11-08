import os
import datetime

##collect all files inside the given path, expan the subdirectories if available
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
##write the body of this function to infect the collected files
def infect(filestoinfect):
    print
    "infecting"

## write this function to do something Benign like printing a message or creating a file in the same folder if certain condition is met
## for example, cetain date or time
def bomb():
    print
    "Bombing"

# the main steps
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
