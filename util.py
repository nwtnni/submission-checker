import os
import shutil

from zipfile import ZipFile
from functools import reduce

def path(f): os.path.join(os.getcwd(), f)
def to_path(s): return reduce(os.path.join, s.split("/"), os.getcwd())
def join(root, f): os.path.join(root, f)

def is_dir(f): return os.path.isdir(f)
def mkdir(f): os.mkdir(f)
def rmdir(f): shutil.rmtree(f)
def rm(f): os.remove(f)

def extract(zf):
    z = ZipFile(zf)
    z.extractall()
    z.close()
    rm(zf)

def walk(f): return os.path.walk(f) 
