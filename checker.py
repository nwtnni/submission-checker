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
                name = rel_path(name, path)
                which = "directory" if is_dir(name) else "file"
                if name not in self.required and not name.endswith(".java"):
                    self.log.append("Found extra " + which + ": " + name)

    def check(self, root):
        previous = cwd(root)
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
