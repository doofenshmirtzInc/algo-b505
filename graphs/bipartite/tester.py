
import sys


def read_file(filename):
    with open(filename, "r") as file:
        groupings = [ [ [int(item) for item in line.split()] for line in group.split('\n') ] for group in ''.join( [line for line in file] ).split('\n\n') ]
        groupings[-1].pop()
        return groupings


def main():

    edgelists = read_file( sys.argv[1] )
    for group in edgelists:
        print(group)
        print()






if __name__ == "__main__":

    if( len(sys.argv) != 3 ):
        raise Exception('usage: ./dijk.py input-file output-file')

    main()

