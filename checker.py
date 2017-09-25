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
                name = join(root, name)
                which = "directory" if is_dir(name) else "file"
                if name not in self.required and not name.endswith(".java"):
                    self.log.append("Found extra " + which + ": " + rel_path(name))

    def required(self):
        msg = "Here's the directory structure we're looking for:\n"
        return msg + arr_to_str(self.required)

    def check(self, root):
        src = path(join(root, "src"))

        if !exists(src):
            return "Please make sure you have a src folder and resubmit.\n\n" + required()
        else:
            previous = cwd(src)

        self.log = []
        self.check_sufficient()
        self.check_necessary(root)
        cwd(previous)
        
        if len(self.log) == 0:
            return "Your submission looks good to go!\n"
        else:
            err = "Oops! Please fix the following errors and resubmit.\n"
            err = err + arr_to_str(self.log) + "\n"
            return err + required()
