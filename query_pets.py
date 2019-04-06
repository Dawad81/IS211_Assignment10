#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


import sqlite3 as lite


con = lite.connect('pets.db')

with con:
    cur = con.cursor()

    while True:
        query_id = raw_input('\nPlease enter a persons ID number, to view '
                             'them and their pets information. \n \n'
                             'Enter [-1] to EXIT the program\n')

        
