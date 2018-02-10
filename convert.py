# -*- coding:utf-8 -*-

import csv
import collections


def main():
    d1 = collections.defaultdict(list)
    with open('../source.csv', 'rb') as csvfile:
        source_file = csv.reader(csvfile, delimiter=',')
        next(source_file, None)
        # ignore header
        # 000001,1999-03,0.007358
        for row in source_file:
            d1[row[0]].append((row[1], row[2]))

    l2 = []
    with open('../dest.csv', 'rb') as csvfile_dest:
        dest_file = csv.reader(csvfile_dest, delimiter=',')
        next(dest_file, None)
        # ignore header
        # 2003-12,600528,2001-05,
        for row in dest_file:
            if row[0]:
                # 2003-12, 600528
                l2.append((row[0], row[1]))

    d3 = collections.defaultdict(list)
    for day, key in l2:
        l = d1[key]
        for i in range(len(l)):
            if l[i][0] == day:
                break
        else:
            print '未找到{}'.format(key)
            break
        for j in range(0 if i - 37 < 0 else i - 37, i):
            d3[(day, key)].append((d1[key][j][0], d1[key][j][1]))

    with open('../result4.csv', 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        for key in d3.keys():
            for a in d3[key]:
                writer.writerow([key[0], key[1], a[0], a[1]])


if __name__ == '__main__':
    main()
