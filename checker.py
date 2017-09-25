from util import *
from functools import reduce

class Checker:

    _REQUIRE_DIR = path("whitelists")

    def __init__(self, assignment):
        with open(join(Checker._REQUIRE_DIR, add_ext(assignment, ".txt")), "r") as f:
            self.required = [line.strip() for line in f]
            self.log = []

    def check_sufficient(self):
        for req in self.required:
            if not exists(req):
                self.log.append("Could not find file or directory: " + req) 

    def check_necessary(self, path):
        for root, dirs, files in walk(path):
            for name in files + dirs:
                print("Before relpath: " + name)
                rel = rel_path(name, path)
                print("After relpath: " + rel)
                which = "directory" if name in dirs else "file"
                if rel not in self.required and not rel.endswith(".java"):
                    self.log.append("Found extra " + which + ": " + rel)

    def check(self, root):

        print("Before: " + pwd())
        previous = cwd(root)
        print("After: " + pwd())
        print("Root: " + root)

        self.log = []
        self.check_sufficient()
        self.check_necessary(root)
        cwd(previous)
        
        if len(self.log) == 0:
            return "Your submission looks good to go!\n"
        else:
            err = "Oops! Please fix the following errors and resubmit.\n"
            err = err + arr_to_str(self.log) + "\n"

            err = err + "Here's the directory structure we're looking for:\n"
            return err + arr_to_str(self.required)
