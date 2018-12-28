#!/bin/python3
# -*- coding: utf-8 -*-

import pandas
data = pandas.read_csv('./annser.csv',
                       header=0,
                       na_values=[''],
                       usecols=[0, 1, 3, 4])
abbrevs = ""
for index, rows in data.iterrows():
    abbrev = "".join(
        [s[:1] for s in (str(rows[1])).split(' ') if s[:1].isupper()]).lower()
    if(str(rows[3]) == 'nan'):
        rows[3] = "?" + abbrev
    abbrevs += "".join([
        "\\DefineJournal{",
        abbrev,
        "}{",
        str(rows[3]),
        "}\n{",
        str(rows[0]),
        "}\n{",
        str(rows[1]),
        "}\n"
    ])
file = open("annser-abbrev.tex", "w")
file.write(abbrevs)
file.close()
