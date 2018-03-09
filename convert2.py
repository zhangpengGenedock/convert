# -*- coding:utf-8 -*-

import csv
import collections
from collections import namedtuple


def main():
    d1 = collections.defaultdict(lambda: collections.defaultdict(str))
    with open('../source.csv', 'rb') as csvfile:
        source_file = csv.reader(csvfile, delimiter=',')
        next(source_file, None)
        # ignore header
        # 000001,2017-09-30 1.06
        for row in source_file:
            v = d1[row[0].zfill(6)][row[1].split('-')[0]]
            if not row[2] and not row[3]:
                continue
            # if (v and float(v) < float(row[2])) or not v:
            d1[row[0].zfill(6)][row[1].split('-')[0]] = (row[2], row[3])

    l2 = []
    with open('../dest.csv', 'rb') as csvfile_dest:
        dest_file = csv.reader(csvfile_dest, delimiter=',')
        next(dest_file, None)
        # ignore header
        for row in dest_file:
            # 600528 2003
            l2.append((row[0].zfill(6), str(int(row[1]) - 1)))

    with open('../result.csv', 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        for key, year in l2:
            v = d1[key][year]
            writer.writerow([key, int(year) + 1, year, v[0], v[1]])


if __name__ == '__main__':
    main()
