from util import *
from functools import reduce

ALLOWED_BY_DEFAULT = ["txt", "java", "pdf", "classpath", "jpg", "png", "DS_Store", "ctr"]

class Checker:

    _REQUIRE_DIR = path("whitelists")

    def __init__(self, assignment):
        with open(join(Checker._REQUIRE_DIR, add_ext(assignment, ".txt")), "r") as f:
            self.all = [line.strip() for line in f]
            self.required = [line.strip().split()[0] for line in f if (line != "" and line[0] != "*")]

    def check_required(self):
        success, missing = [], []
        for req in self.required:
            found = exists(req) or (req.endswith(".txt") and exists(req[:-4] + ".pdf"))
            print(req + " is " found)
            success.append(req) if found else missing.append(req) 

        # Debug
        for s in success:
            print(s)
        for m in missing:
            print(m)
        return (success, missing)

    def check_extra(self, path):
        extra = []
        for root, dirs, files in walk(path):
            for name in files:
                absolute = join(root, name)
                relative = rel_path(absolute, path)
                not_req = relative not in self.required
                not_def = relative.rpartition(".")[2] not in ALLOWED_BY_DEFAULT
                if not_req and not_def:
                    extra.append(relative)
        return extra

    def check(self, root):
        previous = cwd(root)
        success, missing = self.check_required()
        extra = self.check_extra(root)
        cwd(previous)

        if len(success) > 0:
            res = "We scanned your submission and found the following required files:\n"
            res = res + arr_to_str(success) + "\n"
        else:
            res = ""
        
        if len(missing) + len(extra) == 0:
            return res + "\nYour submission looks good to go!\n"

        if len(missing) > 0:
            res = res + "Oops! Looks like you're missing some files:\n"
            res = res + arr_to_str(missing) + "\n"

        if len(extra) > 0:
            res = res + "We've found some extraneous files. Please remove these when you resubmit:\n"
            res = res + arr_to_str(extra) + "\n"

        res = res + "If you think there's an issue with our script, please respond to this email.\n"
        res = res + "For reference, here's the directory structure we're looking for:\n"
        return res + arr_to_str(self.all)
