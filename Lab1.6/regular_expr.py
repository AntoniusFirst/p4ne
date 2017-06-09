import glob
import re

strings=glob.glob(r"E:\Seafile\Seafile\p4ne_training\config_files\*.txt")

def parser (x):
    if re.match("^(.+?)ip address (.+?) (.+?)", x):
        return ("IP", x)
    elif re.match("^interface (.)", x):
        return ("INT", x)
    elif re.match("^hostname (.)", x):
        return ("HOST", x)
    else:
        return ("UNCLASSIFIED", x)

l = []
for i in (strings):
    with open(i) as f:
        for line in (f):
            s = parser(line)
            if s[0] != "UNCLASSIFIED":
                print(s)

