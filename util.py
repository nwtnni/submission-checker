import os
import shutil

from zipfile import ZipFile
from functools import reduce

def arr_to_str(arr): return reduce(lambda a, b: a + b, ["- " + s + "\n" for s in arr])

def exists(f): return os.path.exists(f)

def cwd(path): 
    root = os.getcwd()
    os.chdir(path)
    return root

def pwd(): return os.getcwd()

def add_ext(f, ext): return f + ext

def path(f): return os.path.join(os.getcwd(), f)

def rel_path(f, root): return os.path.relpath(f, root)

def to_path(s, root): return reduce(os.path.join, s.split("/"), root)

def join(root, f): return os.path.join(root, f)

def is_dir(f): return os.path.isdir(f)

def mkdir(f): os.mkdir(f)

def rmdir(f): shutil.rmtree(f)

def rm(f): os.remove(f)

def extract(zf, directory):
    z = ZipFile(zf)
    z.extractall(directory)
    z.close()
    rm(zf)

def walk(f): return os.walk(f) 
