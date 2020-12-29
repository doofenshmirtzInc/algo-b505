def parse_file(infile):
    with open(infile) as f:
        lines = f.readlines()

    arrays = []
    arrays.extend(
        [int(elem) for line in lines for elem in line.split()]
    )

    return arrays

