#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring."""


import sqlite3 as lite


con = lite.connect('pets.db')

with con:
    cur = con.cursor()

    while True:
        query_id = raw_input("\nPlease enter a persons ID number, to view "
                             "them and their pets information. \n \n"
                             "Enter [-1] to EXIT the program\n")
        
        cur.execute("SELECT * FROM person WHERE person.id = (?)", (query_id)) #, pet, person_pet")
    #rows = cur.fetchall()
    #while True:

        rows = cur.fetchall()

    #if row == None:
        #break
        for row in rows:
            print row
