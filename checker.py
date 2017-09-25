from util import *
from functools import reduce

class Checker:

    _REQUIRE_DIR = path("whitelists")

    def __init__(self, assignment):
        with open(join(Checker._REQUIRE_DIR, add_ext(assignment, ".txt")), "r") as f:
            self.required = [line.strip() for line in f]
            self.log = []
            self.success = []

    def check_sufficient(self):
        for req in self.required:
            if req[0] == "*":
                found = True
            elif req.endswith(".txt"):
                found = exists(req) or exists(req[:-4] + ".pdf")
            else:
                found = exists(req)

            if found:
                self.success.append("Found: " + req)
            else:
                self.log.append("Could not find: " + req) 

    def check_necessary(self, path):
        for root, dirs, files in walk(path):
            for name in files + dirs:
                which = "directory" if name in dirs else "file"
                absolute = join(root, name)
                relative = rel_path(absolute, path)

                not_req = relative not in self.required
                not_java = not name.endswith(".java")
                not_pdf = not relative[:-4] + ".txt" in self.required

                if not_req and not_java and not_pdf:
                    self.log.append("Found extra " + which + ": " + relative)

    def check(self, root):
        previous = cwd(root)
        self.log = []
        self.success = []
        self.check_sufficient()
        self.check_necessary(root)
        cwd(previous)

        if len(self.success) > 0:
            res = "We scanned your submission and found the following required files:\n"
            res = result + arr_to_str(self.success) + "\n"
        else:
            res = ""
        
        if len(self.log) == 0:
            res = res + "\nYour submission looks good to go!\n"
        else:
            res = res + "Oops! We may have found some errors (or our submission checker is buggy).\n"
            res = res + "Please check over the log, and resubmit if necessary:\n"
            res = res + arr_to_str(self.log) + "\n"
            res = res + "For reference, here's the directory structure we're looking for:\n"
            res = res + arr_to_str(self.required)
        return res
