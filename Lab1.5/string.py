import glob

strings=glob.glob(r"E:\Seafile\Seafile\p4ne_training\config_files\*.txt")

l = []
for i in (strings):
    with open(i) as f:
        for line in (f):
            if line.find('ip address') == 1:

                l.append(line.strip())

l = list(set(l))
print(l)







