#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os.path as path
import csv


def collect(csv_path, columns=None, encoding='utf8'):
    result = []
    with open(csv_path, encoding=encoding) as csv_file:
        reader = csv.DictReader(csv_file)
        try:
            for row in reader:
                if not columns:
                    data = tuple(row.values())
                else:
                    data = tuple(row[column] for column in columns)
                #print('data:', data)
                result.append(data)
        except e:
            print(e)
    return result


if __name__ == '__main__':
    try:
        csv_path = sys.argv[1]
    except:
        sys.stderr.write('Usage: {} /path/to/csv\n'.format(
            sys.argv[0]))
        sys.exit(1)

    columns=['支行信息', 'BDC正确支行名称', '内部编码']
    template = '''update GE_SYS_CUSTOMER_CHARGE_INFO set BDC_BANK_CODE='{2}',SUB_BANK='{1}' where BDC_BANK_CODE is null and SUB_BANK='{0}';'''

    custs = collect(path.expanduser(csv_path), columns=columns, encoding='gbk')
    print('\n'.join((template.format(*data) for data in custs)))
