import math
import operator

import sys
sys.path.append('..')

from heapq import heappush, heappop
from functools import reduce
from pathlib import Path

import common as aoc
from aocd import get_data


def solve(inp):
    pass


if __name__ == '__main__':
    #inp = aoc.readgridnums(Path('sample.txt'))
    inp = aoc.readgridnums(get_data(day=17, year=2024))
    print(solve(inp))
