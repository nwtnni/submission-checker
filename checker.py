from util import *
from functools import reduce

class Checker:

    _REQUIRE_DIR = path("requirements")

    def __init__(self, assignment, root):
        with open(join(Checker._REQUIRE_DIR, add_ext(assignment, ".txt")), "r") as f:
            self.required = [to_path(line, root) for line in f]

            for req in self.required:
                print(req)

            self.root = root
            self.log = []

    def check_sufficient(self):
        for req in self.required:
            if not exists(req):
                self.log.append("Could not find file or directory: " + req) 

    def check_necessary(self):
        for root, dirs, files in walk(self.root):
            for name in files + dirs:
                name = join(root, name)
                which = "directory" if is_dir(name) else "file"
                if name not in self.required:
                    self.log.append("Found extra " + which + ": " + name)

    def check(self):
        self.check_sufficient()
        self.check_necessary()
        
        if len(self.log) == 0:
            return "Your submission looks good to go!\n"
        else:
            err = reduce(lambda a, b: a + b + "\n", self.log)
            return "Oops! Please fix the following errors and resubmit.\n" + err
