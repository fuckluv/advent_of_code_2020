
def parse_pass_batch(stream):
    current_pass = []
    for l in stream.splitlines():
        if l == "":
            yield " ".join(current_pass)
            current_pass = []
        else:
            current_pass.append(l.strip())
    yield " ".join(current_pass) #last pass


def read_pass_batch(path):
    pass()
