#author: jack mcshane
#term: fall 2020

"""
this program determines the minimum edit distance (i.e. least number of insertions,
deletions, and mismatches) between two words. This algorithm of calculating the
minimum edit distance in implemented using the dynammic programming paradigm
"""

import sys

#parse the given input file
def parse_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    values = []
    values.extend(
        [str(elem) for line in lines for elem in line.split()]
    )

    return values



#calculate the edit distance between one_str and two_str
def edit_dist(one_str, two_str):
    rows, cols = (len(one_str) + 1, len(two_str) + 1)
    dist = [[None for col in range(cols)] for row in range(rows)]
    for i in range(len(dist)):
        dist[i][0] = i
    for j in range(len(dist[0])):
        dist[0][j] = j


    for j in range(1, len(two_str) + 1):
        for i in range(1, len(one_str) + 1):
            insertion = dist[i][j-1] + 1
            deletion = dist[i-1][j] + 1
            mismatch = dist[i-1][j-1] + 1
            match = dist[i-1][j-1]
            if one_str[i-1] == two_str[j-1]:
                dist[i][j] = min(insertion, deletion, match)
            else:
                dist[i][j] = min(insertion, deletion, mismatch)

    return dist[len(one_str)][len(two_str)]



#driver code
filename = sys.argv[1]
one_str, two_str = parse_file(filename)
print(edit_dist(one_str, two_str))
