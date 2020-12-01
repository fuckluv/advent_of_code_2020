from itertools import combinations

def find_pair_given_sum(l, expected_sum):
    """
      Finds in a list a pair of values for which the sum is equal to
      "expected_sum". Returns the first pair found (in ascending order of
      indexes), or None if none is found
    """
    if len(l) > 0:
        for combination in combinations(l, 2):
            if sum(combination) == expected_sum:
                return combination
    return None


def find_trio_given_sum(l, expected_sum):
    """
      Finds in a list a trio of indexes for which the sum of values is sum
      returns the first trio found (in ascending order), or None if none is found
    """
    if len(l) > 1:
        for combination in combinations(l, 3):
            if sum(combination) == expected_sum:
                return combination
    return None

def read_input(path):
    file = open(path)
    input = [int(i) for i in file.read().splitlines()]
    file.close()
    return(input)

def print_solution(solution, problem):
    product = 1
    for s in solution:
        product *= s
    print(
        f'Solution {problem}\n'
        f'------------\n'
        f'Sum of {solution} is {sum(solution)}\n'
        f'Product of {solution} is {product}'
    )

if __name__ == '__main__':
    l = read_input("./input.txt")
    sol1a = find_pair_given_sum(l, 2020)
    print_solution(sol1a, "1A")
    sol2a = find_trio_given_sum(l, 2020)
    print_solution(sol2a, "2A")
