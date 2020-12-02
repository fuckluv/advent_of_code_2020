import pandas as pd
import operator

def read_input(path):
    df_input = pd.read_csv(
        path,
        sep = '-|\s+|:\s',
        engine = 'python',
        names = ['min_char', 'max_char', 'char', 'password']
    )
    return df_input

def is_policy_compliantA(pw_dict):
    n = pw_dict["password"].count(pw_dict["char"])
    return n >= pw_dict["min_char"] and n <= pw_dict["max_char"]

def is_policy_compliantB(pw_dict):
    letters = [pw_dict["password"][i - 1] \
            for i in (pw_dict["min_char"], pw_dict["max_char"])]
    return operator.xor(*(l == pw_dict["char"] for l in letters))

def print_solution(compliance, problem):
    print(
        f'Solution to problem {problem}:\n'
        f'----------------------\n'
        f'Number of compliant pw: {sum(compliance)}\n'
        f'Not compliant pw: {len(compliance) - sum(compliance)}\n'
        )

if __name__ == "__main__":
    input_df = read_input("input.txt")
    complianceA = input_df.apply(is_policy_compliantA, axis = 1)
    print_solution(complianceA, "2A")

    print()
    complianceB = input_df.apply(is_policy_compliantB, axis = 1)
    print_solution(complianceB, "2B")
