#!/usr/bin/env python3

#
# Copyright 2013 Simone Campagna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__author__ = 'Simone Campagna'
from .debug import PRINT

def show_title(title, print_function=PRINT, max_width=70):
    t = "==[{0}]".format(title)
    t += "=" * (max_width - len(t))
    print_function(t)

def show_table(title, table, min_number=3, separator=' ', print_function=PRINT, show_always_title=False, header=None):
    new_table = []
    if header:
        h_table = [header] + list(table)
    else:
        h_table = table
    for row in h_table:
        if isinstance(row, (tuple, list)):
            new_table.append(tuple(str(item) for item in row))
        elif isinstance(row, str):
            new_table.append((row, ))
        else:
            new_table.append((str(row), ))
    table = new_table

    if title and (show_always_title or table):
        show_title("{0} ({1})".format(title, len(table)))

    if not table:
        return

    num_cols = set(len(row) for row in table)
    max_num_cols = max(num_cols)
    if len(num_cols) > 1:
        new_table = []
        for row in table:
            if len(row) < max_num_cols:
                row += tuple('' for i in range(max_num_cols - len(row)))
            new_table.append(row)
        table = new_table

    max_lengths = [max(len(row[col]) for row in table) for col in range(max_num_cols)]
    mods = []
    for max_length in max_lengths[:-1]:
        if max_length:
            mods.append(":{0}s".format(max_length))
        else:
            mods.append("")
    mods.append("")

    if header:
        header = table.pop(0)

    fmts = ["{{{i}{m}}}".format(i=i + 1, m=m) for i, m in enumerate(mods)]
    fmt = separator.join(fmts)

    l = max(len(str(len(table) - 1)), min_number)
    r_fmt = '{{0:{l}d}}) '.format(l=l) + fmt

    if header:
        h_fmt = '{{0:{l}s}}  '.format(l=l) + fmt
        print_function(h_fmt.format("", *header))
        
    for i, row in enumerate(table):
        print_function(r_fmt.format(i, *row))
