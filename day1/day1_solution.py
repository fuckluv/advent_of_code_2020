def find_pair_given_sum(l, expected_sum):
    """
      Finds in a list a pair of indexes for which the sum of values is sum
      returns the first pair found (in ascending order), or None if none is
      found
    """
    if len(l) > 0:
        for i, x in enumerate(l[:-1]):
            for j, y in enumerate(l[i + 1:]):
                if x + y == expected_sum:
                    return (i, j + i + 1)
    return None


def find_trio_given_sum(l, expected_sum):
    """
      Finds in a list a trio of indexes for which the sum of values is sum
      returns the first trio found (in ascending order), or None if none is found
    """
    if len(l) > 1:
        for i, x in enumerate(l[:-1]):
            for j, y in enumerate(l[i + 1:]):
                for k, z in enumerate(l[i + j + 2:]):
                    if x + y + z == expected_sum:
                        return (i, j + i + 1, k + j + i + 2)
    return None

def read_input(path):
    file = open(path)
    input = [int(i) for i in file.read().splitlines()]
    file.close()
    return(input)

if __name__ == '__main__':
    l = read_input("./input.txt")
    print(len(l))
    i, j = find_pair_given_sum(l, 2020)
    print(
        f'Solution 1a:\n'
        f'------------\n'
        f'The product of {l[i]} (index {i}) and {l[j]} (index {j})'
        f'gives {l[i] * l[j]}'
    )
    i, j, k = find_trio_given_sum(l, 2020)
    print()
    print(
        f'Solution 1b:\n'
        f'------------\n'
        f'The product of {l[i]} (index {i}) and {l[j]} (index {j}) and '
        f'{l[k]} (index {k}) gives '
        f'{l[i] * l[j] * l[k]}'
    )
