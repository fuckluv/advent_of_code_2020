
def parse_pass_batch(text):
    """
    Returns a genarator of passes read from a "text" (accepting
    `splitlines()` method), where each pass is one string (with newlines
    stripped, and space separated values)
    """
    current_pass = []
    for l in text.splitlines():
        if l == "":
            yield " ".join(current_pass)
            current_pass = []
        else:
            current_pass.append(l.strip())
    yield " ".join(current_pass) #last pass


def read_pass_batch(path):
    """Returns a generator of passes from a file located at "path" """
    with open(path) as f:
        return parse_pass_batch(f.read())

def is_valid_pass(passport):
    """Checks if a passport (`string`) is valid or not"""
    compulsary_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    if all([passport.find(f + ":") >= 0 for f in compulsary_fields]): \
        return True
    return False
