# -*- coding:utf-8 -*-

import csv
import collections


def main():
    d1 = collections.defaultdict(lambda: collections.defaultdict(str))
    with open('../data/src.csv', 'rb') as csvfile:
        source_file = csv.reader(csvfile, delimiter=',')
        next(source_file, None)
        # ignore header
        # 000001,1999-03,0.007358
        for row in source_file:
            d1[row[0]][row[1].split('-')[0]] = row[2]

    l2 = []
    with open('../data/dest.csv', 'rb') as csvfile_dest:
        dest_file = csv.reader(csvfile_dest, delimiter=',')
        next(dest_file, None)
        # ignore header
        for row in dest_file:
            if row and row[0]:
                # 600528, 2001
                l2.append((row[0]))

    # d3 = collections.defaultdict(list)
    # for day, key in l2:
    #     l = d1[key]
    #     for i in range(len(l)):
    #         if l[i][0] == day:
    #             break
    #     else:
    #         print '未找到{}'.format(key)
    #         break
    #     for j in range(0 if i - 37 < 0 else i - 37, i):
    #         d3[(day, key)].append((d1[key][j][0], d1[key][j][1]))

    with open('../data/result4.csv', 'wb') as f:
        writer = csv.writer(f, delimiter=',')
        for key in l2:
            try:
                for v in sorted(d1[key]):
                    writer.writerow([key, v, d1[key][v]])
            except:
                writer.writerow([key, '', ''])


if __name__ == '__main__':
    main()
