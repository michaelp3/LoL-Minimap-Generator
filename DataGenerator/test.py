from importlib.resources import path
import os, random
path = "Blue/"
files = os.listdir(path)
d = random.choice(files)
d = d[:-4]
print(d)