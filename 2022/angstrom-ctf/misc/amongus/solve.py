from os import walk
from os.path import join

parent_path = './out'

for root, dirs, files in walk(parent_path):
    files = files
print(files)
print(len(files))

pattern = 'b910c1c37'
for f in files:
    f = join(parent_path, f)
    with open(f, 'r') as fp:
        data = fp.read(len(pattern))
        if data != pattern:
            print(f)
