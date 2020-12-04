import pandas as pd
from numpy import nan
import re

def split_pass_batch(text):
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

def parse_pass(pass_str):
    """Takes a pass_str string and convert it into a dictionnary"""
    fields = str.split(pass_str, " ")
    pass_dict = {}
    for field in fields:
        pass_dict[field[:3]] = field[4:]
    return pass_dict


def read_pass_batch(path):
    """Returns a generator of passes from a file located at "path" """
    with open(path) as f:
        pass_df = pd.DataFrame([parse_pass(p) \
                for p in split_pass_batch(f.read())])
        return pass_df

def are_valid_passes_1A(passes):
    """Checks if a passes (`pd.DataFrame`) is valid or not"""
    compulsary_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return ~ passes[compulsary_fields].isnull().any(axis = 1)

def  is_between(passes, field, min, max):
    return  pd.to_numeric(passes[field], errors = "coerce").ge(min) &\
            pd.to_numeric(passes[field], errors = "coerce").le(max)

def valid_hgt(hgt):
    cm_or_in

def are_valid_passes_1B(p):
    p["valid_1A"] = are_valid_passes_1A(p)
    p["valid_byr"] = is_between(p, "byr", 1920, 2002)
    p["valid_iyr"] = is_between(p, "iyr", 2010, 2020)
    p["valid_eyr"] = is_between(p, "eyr", 2020, 2030)
    p["hgt_unit"] = p["hgt"].str.extract("(\D+)")
    p["hgt_msr"] = p["hgt"].str.extract("(\d+)")
    p["valid_hgt"] =  \
            (p["hgt_unit"].eq("cm") & is_between(p, "hgt_msr", 150, 193)) | \
            (p["hgt_unit"].eq("in") & is_between(p, "hgt_msr", 59, 76))
    p["valid_hcl"] = p["hcl"].str.match("#[a-f0-9]{6}")
    p["valid_ecl"] = p["ecl"].isin( \
            ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    p["valid_pid"] = p["pid"].str.match("^\d{9}$")
    return p.loc[:, p.columns.str.startswith("valid")].all(axis = 1)

if __name__ == "__main__":
    passes = read_pass_batch("./input.txt")
    solution_4A = sum(are_valid_passes_1A(passes))
    print(
            f'Solution 4A:\n'
            f'------------\n'
            f'{solution_4A} valid passes out of {passes.shape[0]}'
            )
    solution_4B = sum(are_valid_passes_1B(passes))
    print()
    print(
            f'Solution 4B:\n'
            f'------------\n'
            f'{solution_4B} valid passes out of {passes.shape[0]}'
            )

