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
        cur.execute("SELECT first_name, last_name, person.age, name, breed, "
                    "pet.age, dead FROM person, pet, person_pet "
                    "WHERE person_id = person.id AND"
                    " pet_id = pet.id AND person_pet.person_id = (?)", (query_id))

        rows = cur.fetchall()

        print rows

        for row in rows:
            print '{} {}, {} years old'.format(row[0], row[1], row[2])
            if row[6] == 1:
                #print '{} {}, {} years old'.format(row[0], row[1], row[2])
                print '{} {} currently owns {}, a {}, that is {} years old.'.format(row[0],row[1],row[3],row[4],row[5])
            else:
                print '{} {} owned {}, a {}, that passed away at the age of {}.'.format(row[0],row[1],row[3],row[4],row[5])
